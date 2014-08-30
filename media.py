import soundcloud

class Player(object):

    def __init__(self):
        self.client = soundcloud.Client(client_id="REMOVED FOR SECURITY PURPOSES")
        self.user_id = "REMOVED"
        
    def get_url(self, resource):
        """Grabs the permalink for whatever SoundCloud resource you'd like.
        For example, for the latest track, choose the '/tracks' resource.
        See developers.soundcloud.com/docs/api/reference for more info."""
        
        info = self.client.get(resource, user_id=self.user_id)
        url = info[0].obj['permalink_url']
        
        return url
        
    
    def player(self, track_url, width="325px", height=None):
        """The actual Soundcloud player"""
        embed_info = self.client.get('/oembed',
                                     url=track_url,
                                     maxwidth=width,
                                     maxheight=height)
        
        return embed_info.obj['html']