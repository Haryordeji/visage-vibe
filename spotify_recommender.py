import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

class SpotifyRecommender:
    def __init__(self):
        self.spotify = self.setup_spotify()
        self.emotion_genre_map = {
            'Angry': 'rock',
            'Disgust': 'metal',
            'Fear': 'ambient',
            'Happy': 'pop',
            'Sad': 'blues',
            'Surprise': 'electronic',
            'Neutral': 'classical'
        }

    def setup_spotify(self):
        client_credentials_manager = SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET
        )
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_recommendations(self, emotion):
        genre = self.emotion_genre_map.get(emotion, 'pop')
        results = self.spotify.recommendations(seed_genres=[genre], limit=5)
        
        recommendations = []
        for track in results['tracks']:
            recommendations.append({
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'album': track['album']['name'],
                'cover_url': track['album']['images'][0]['url'] if track['album']['images'] else None
            })
        
        return recommendations