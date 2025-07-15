import unittest
from app.topic_manager import TopicManager

class TestTopicManager(unittest.TestCase):
    def test_find_highest_score_in_empty_list(self):
        #Arrange
        scores=[]
        cut = TopicManager()
        expected_result = []

        #Act
        result=cut.find_topic_high_scores(scores)

        #Assert
        self.assertEqual(result,expected_result)

if __name__ == '__main__':
    unittest.main()
