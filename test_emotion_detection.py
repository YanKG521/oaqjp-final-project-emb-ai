import unittest
from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        testdic = {
            "joy" : "I am glad this happened",
            "anger" : "I am really mad about this",
            "disgust" : "I feel disgusted just hearing about this",
            "sadness" : "I am so sad about this",
            "fear" : "I am really afraid that this will happen"
        }
        for emotion, statement in testdic.items():
            result = emotion_detector(statement)
            self.assertEqual(result['dominant_emotion'], emotion)

unittest.main()