from app import app
from unittest import TestCase

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class ConversionTestCase(TestCase):
    # Unit Tests #
        
    def test_index(self):
        with app.test_client() as client:
            res = client.get('/playlists')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code,200)  #testing status code
            self.assertIn('See all the playlists!',html)  #testing index.html label
    
    def test_wtforms(self):
        with app.test_client() as client:
            res = client.get('/playlists/add')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code,200)  #testing status code
            self.assertIn('Playlist Description (Optional)',html)  #testing index.html label
            