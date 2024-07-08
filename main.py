from emotion_detector import EmotionDetector
from spotify_recommender import SpotifyRecommender

class MoodMusicRecommender:
    def __init__(self):
        self.emotion_detector = EmotionDetector()
        self.spotify_recommender = SpotifyRecommender()

    def run(self):
        emotion = self.emotion_detector.capture_emotion()
        if emotion:
            print(f"Detected emotion: {emotion}")
            recommendations = self.spotify_recommender.get_recommendations(emotion)
            for i, track in enumerate(recommendations, 1):
                print(f"{i}. {track['name']} by {track['artist']} from {track['album']}")
        else:
            print("No emotion detected. Please try again.")

if __name__ == "__main__":
    recommender = MoodMusicRecommender()
    recommender.run()