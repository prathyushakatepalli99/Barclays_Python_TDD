class TopicTopScore:
    def __init__(self,topic_name , top_score):
        self._topic_name = topic_name
        self._top_score = top_score

    def get_topic_name(self):
        return self._topic_name

    def get_top_score(self):
        return self._top_score


