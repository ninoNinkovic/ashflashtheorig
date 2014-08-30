from wtforms import Form, BooleanField, TextField, TextAreaField, validators
from flask_mail import Mail, Message
from ashflash import app


mail = Mail(app)


# Custom Validator for honeypot
# Robots usually check all checkboxes, thinking its an agreement of terms.
# However, if the checkbox IS checked, the email won't go through.
def validate_honeypot(form, field):
    if field.data:
        raise validators.ValidationError('This checkbox must NOT be checked.')
        
        
class ContactForm(Form):
    name = TextField('Name', [validators.Length(min=1, max=35)])
    email = TextField('Email Address',
                      [validators.Email(), validators.Required()])
    subject = TextField('Subject')
    message = TextAreaField('Your Message',
                            [validators.Length(min=5, max=140),
                             validators.Required()])
    # Will be hidden by CSS
    honeypot = BooleanField('Do not click if you are human',
                            [validate_honeypot])
                            
    
    def send(self):
        msg = Message(self.subject.data,
                      recipients=[app.config['MAIL_USERNAME']],
                      sender=self.email.data)
        msg.body = "From: %s\n\nMessage:\n%s\n\nSender's Email:\n%s" % (self.name.data, self.message.data, self.email.data)
        mail.send(msg)