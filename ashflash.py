"""
    AshFlashtheOrig.net
    ~~~~~~~~~~~~~~~~~~~

    AshFlash's website which serves as a hub to other interactive media hosted on
    sites like YouTube, Soundcloud, Twitter and Facebook.

    :copyright: (c) 2012 by Ash Courchene

"""

from flask import Flask
from media import Player

#App setup
app = Flask(__name__)
app.secret_key = 'REMOVED FOR SECURITY PURPOSES'

if app.config['DEBUG']:
    from werkzeug import SharedDataMiddleware
    import os
    
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/': os.path.join(os.path.dirname(__file__), 'static')})

#Custom template functions
p = Player()
track_url = p.get_url('/tracks')
set_url = p.get_url('/playlists')

# Set up SoundCloud playlist for templating system
app.jinja_env.globals.update(latest_track=p.player(track_url),
                             setlist=p.player(set_url,
                                              width="900px",
                                              height="320px"))

#Config
app.config.update(
    #Email Setting
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'ash.courchene@gmail.com',
    MAIL_PASSWORD = 'REMOVED FOR SECURITY PURPOSES'
)
