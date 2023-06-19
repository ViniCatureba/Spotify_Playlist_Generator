import json
import unittest
from flask import Flask
from main import app


class SpotifyAPITest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_callback(self):
        response = self.app.get('/callback')
        self.assertEqual(response.status_code, 302)

    def test_create_playlists(self):
        with self.app:
            self.app.get('/callback')
            with self.app.session_transaction() as session:
                session['access_token'] = get_access_token_from_cache()
            response = self.app.get('/create-playlist')
            self.assertEqual(response.status_code, 200)

    def test_logoff(self):
        response = self.app.post('/logoff')
        self.assertEqual(response.status_code, 302)

    def test_faq(self):
        response = self.app.get('/faq')
        self.assertEqual(response.status_code, 200)

    def test_about_us(self):
        response = self.app.get('/aboutus')
        self.assertEqual(response.status_code, 200)

    def test_create_playlist_html(self):
        response = self.app.get('/createPlaylist')
        self.assertEqual(response.status_code, 200)

def get_access_token_from_cache():
    with open('.cache', 'r') as file:
        cache_data = json.load(file)
        return cache_data['access_token']


if __name__ == '__main__':
    unittest.main()
