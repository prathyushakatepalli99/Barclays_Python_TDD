import unittest
from app.topic_manager import TopicManager
from app.topic_scores   import TopicScores
from app.topic_top_score import TopicTopScore


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


    def test_find_highest_score_with_list_of_one_returns_list_of_one(self):  #Arrange
        scores=[45,56,67,99]
        topic_name="Physics"
        topic_scores =[TopicScores(topic_name,scores)]

        cut = TopicManager()

        expected_result = [TopicTopScore(topic_name,99)]

        #Act
        result=cut.find_topic_high_scores(topic_scores)

        #Assert
        self.assertEqual(result[0].get_topic_name(),expected_result[0].get_topic_name())
        self.assertEqual(result[0].get_topic_score(),expected_result[0].get_topic_score())



if __name__ == '__main__':
    unittest.main()

