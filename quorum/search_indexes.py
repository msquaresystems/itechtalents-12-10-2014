#search_indexes.py
import datetime
from haystack import indexes
from quorum.models import Question
class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    question = indexes.CharField(model_attr='question')
    topic = indexes.CharField(model_attr='topic')    
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Question

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created__lte=datetime.datetime.now())