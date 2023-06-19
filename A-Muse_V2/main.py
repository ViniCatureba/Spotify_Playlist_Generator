from flask import Flask, render_template, redirect, session, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

CLIENT_ID = '0037befdbf8e49db9fd98643c00a010b'
CLIENT_SECRET = 'e324ec3d023a4f138e93fce9542f91b8'
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPE = 'user-top-read playlist-modify-private'


sp_oauth = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/callback')
def callback():
    code = request.args.get('code')

    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']

    session['access_token'] = access_token

    return redirect('/')





@app.route('/create-playlist')
def create_playlists():
    if 'access_token' in session:
        sp = spotipy.Spotify(auth=session['access_token'])

        top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')
        recommended_tracks = sp.recommendations(seed_tracks=[track['id'] for track in top_tracks['items'][:5]], limit=5)['tracks']

       
        recommended_track_uris = [track['uri'] for track in recommended_tracks]

        
        recommended_playlist = sp.user_playlist_create(sp.current_user()['id'], 'Recomendadas', public=False)

        
        sp.user_playlist_add_tracks(sp.current_user()['id'], recommended_playlist['id'], recommended_track_uris)

        return render_template('playlistCriada.html')
    else:
        return redirect('/')


@app.route('/logoff', methods=['POST'])
def logoff():
    session.pop('access_token', None)
    os.remove(".cache")

    return redirect('/')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutUs.html')

@app.route('/createPlaylist')
def createplaylistHtml():
    return render_template('createplaylist.html')




if __name__ == '__main__':
    app.run(debug=True)
