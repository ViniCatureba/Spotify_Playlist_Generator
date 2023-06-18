import unittest
from flask import Flask
from main import app


class SpotifyAPITest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)  

    def test_callback(self):
        response = self.app.get('/callback')
        self.assertEqual(response.status_code, 200)  

    def test_top_tracks(self):
        with self.app:
            self.app.get('/callback')
            with self.app.session_transaction() as session:
                session['access_token'] = 'token_qualquer'
            response = self.app.get('/top-tracks')
            self.assertEqual(response.status_code, 404)  

    def test_create_playlist(self):
        with self.app:
            self.app.get('/callback')
            with self.app.session_transaction() as session:
                session['access_token'] = 'token_qualquer'
            response = self.app.get('/create-playlist')
            self.assertEqual(response.status_code, 404)  


if __name__ == '__main__':
    unittest.main()
