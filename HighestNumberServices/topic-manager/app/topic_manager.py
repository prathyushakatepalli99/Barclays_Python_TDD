import os
import sys
from app.topic_top_score import TopicTopScore

mpath = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","find-highest-number"))
sys.path.insert(0,mpath)

from app.highest_number_finder import HighestNumberFinder


class TopicManager:
    def __init__(self):
        self._highest_number_finder = HighestNumberFinder()

    def find_topic_high_scores(self,topic_scores_list):
      top_scores=[]
      return top_scores
