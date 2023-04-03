from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        fq = Question(pub_date=timezone.now() + timedelta(days=30))
        self.assertIs(fq.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - timedelta(days=1, seconds=1)
        oq = Question(pub_date=time)
        self.assertIs(oq.was_published_recently(), False)

    def test_was_published_recently_with_recent_qu(self):
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
        recent_qu = Question(pub_date=time)
        self.assertIs(recent_qu.was_published_recently(), True)
