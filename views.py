from flask import Flask, render_template, request, flash
from twit_list import get_tweets
from forms import ContactForm
from ashflash import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
				tweets = get_tweets()
				return render_template('index.html', tweets=tweets)
        
@app.route('/biography')
def biography():
    return render_template('biography.html')
        
@app.route('/media')
def media():
    return render_template('media.html')
        
@app.route('/contact', methods=['GET', 'POST'])
def contact():
				form = ContactForm(request.form)
				if request.method=='POST' and form.validate():
								form.send()
								flash("<p>Thanks for your email. I'll get back to you as soon as I can.</p><p>Click here to return to the <a href='/' id='thanks'>main page</a></p>")
				return render_template('contact.html', form=form)
 
    
if __name__ == '__main__':
    app.run()
