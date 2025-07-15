import unittest
from app.topic_manager import TopicManager
from app.topic_scores   import TopicScores
from app.topic_top_score import TopicTopScore

#Create a Test 'STUNT' Double using a STUB
class StubHighestNumberFinder:
    def find_highest_number(self,number):
        return 89 #PRE-DEFINED fixed result


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



    def test_find_highest_score_with_one_topic_using_stud(self):
        scores = [45, 56, 67, 89]
        topic_name = "Physics"
        topic_scores = [TopicScores(topic_name, scores)]

       # cut = TopicManager()
        hnf_stub = StubHighestNumberFinder()
        cut = TopicManager(hnf_stub)
        expected_result = [TopicTopScore(topic_name, 89)]

        # Act
        result = cut.find_topic_high_scores(topic_scores)

        # Assert
        self.assertEqual(result[0].get_topic_name(), expected_result[0].get_topic_name())
        self.assertEqual(result[0].get_topic_score(), expected_result[0].get_topic_score())


    def test_find_highest_score_with_list_of_many_topics_returns_list_of_many_using_stubs(self):
        #ARRANGE
        physics_scores =[56,67,45,89]
        art_scores =[87,66,78]
        compsci_scores =[45,88,97,56]
        topi_scores =[TopicScores("Physics",physics_scores), TopicScores("Art",art_scores),TopicScores("Compsci",compsci_scores)]
        expected_results =[TopicScores("Physics",89), TopicScores("Art",89),TopicScores("Compsci",89)]
        hnf_stub = StubHighestNumberFinder()
        cut = TopicManager(hnf_stub)

        #ACT
        result = cut.find_topic_high_scores(topi_scores)

        #ASSERT
        for i in range(len(expected_results)):
            self.assertEqual(result[i].get_topic_name(), expected_result[i].get_topic_name())
            self.assertEqual(result[i].get_top_score(), expected_result[i].get_top_score())



if __name__ == '__main__':
    unittest.main()

