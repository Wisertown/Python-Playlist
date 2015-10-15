import re
import time
from time import mktime
from datetime import datetime
from system.core.controller import *
import re
import time
from time import mktime
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
# app.secret_key = "the secret way to do stuff"


class Songs(Controller):
    def __init__(self, action):
        super(Songs, self).__init__(action)

        self.load_model('Song')

    def index(self):
        return self.load_view('dashboard.html')

    def add_song(self):
    	song_details = request.form
    	result = self.models['Song'].add_song(song_details)
    	if result['status'] == True:
    		for msg in result['success']:
            		flash(msg)
            	return redirect('/show')
    
    def show(self):
    	songs = self.models['Song'].get_all_songs()
    	return self.load_view('dashboard.html', songs=songs)

    def add_to_list(self, id):
        playlist = self.models['Song'].add_to_list(id)
        if playlist['status'] == True:
            for msg in playlist['success']:
                flash(msg)
            return redirect('/show')

    def user_playlist(self, id):
        play_list = self.models['Song'].user_playlist(id)
        return self.load_view('playlist.html', play=play_list)

    def show_song_info(self, id):
        songtitle = self.models['Song'].song_title(id)
        song_detail = self.models['Song'].songs_added(id)
        song_add_count =  self.models['Song'].add_count(id)
        return self.load_view('viewothers.html', details=song_detail, counts=song_add_count, pongs=songtitle)



    def logout(self):
    	session.clear
    	return redirect('/')
