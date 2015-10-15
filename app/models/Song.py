from flask import Flask, render_template, redirect, url_for, session, request, flash
import re
import time
from time import mktime
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
from system.core.model import Model




class Song(Model):
    def __init__(self):
        super(Song, self).__init__()

    
    def add_song(self, song_details):
    	success = []
    	success.append("Congratulations! song added to the database")
    	insert_song_query = "INSERT INTO songs (title, artist, added, created_at, updated_at) Values ('{}', '{}', NOW(), NOW())".format(song_details['title'], song_details['artist'])
    	return self.db.query_db(insert_song_query)

    def get_all_songs(self):
        get_all_song_query = "SELECT COUNT(playlist.added)as count, songs.title, songs.artist, songs.id FROM songs LEFT JOIN playlist ON songs.id = playlist.song_id GROUP BY songs.id"

        get_everything_query = "SELECT * from songs"
        return self.db.query_db(get_all_song_query)

    def add_to_list(self, id):
        success = []
        success.append("Congratulations! song added to the playlist") 
        add_playlist_query = "INSERT into playlist (user_id, song_id, added, created_at, updated_at) Values  ('{}', '{}', 1, NOW(), NOW())".format(session['id'], id)
        self.db.query_db(add_playlist_query)
        return {'status': True, 'success': success}


    def songs_added(self, id):
        others_added_query = "SELECT COUNT(playlist.added)as count, users.id, users.first_name, users.last_name FROM users INNER JOIN playlist ON users.id = playlist.user_id where song_id = '{}' GROUP by user_id".format(id)
        return self.db.query_db(others_added_query)

    def song_title(self, id):
        get_songtitle_query = "SELECT title, artist from songs where id = '{}'".format(id) 
        return self.db.query_db(get_songtitle_query)

    def add_count(self, id):
        get_count_query = "SELECT COUNT(*) as total from playlist where song_id = '{}'".format(id)
        return self.db.query_db(get_count_query)
    
    def user_playlist(self, id):
        get_playlist = "SELECT DISTINCT users.id, users.first_name, users.last_name, songs.artist, songs.title, sum(playlist.added)%10 as total FROM users JOIN playlist on users.id = playlist.user_id JOIN songs on playlist.song_id = songs.id WHERE user_id = '{}' GROUP by song_id".format(id)
        return self.db.query_db(get_playlist)


        
    	

        
        


