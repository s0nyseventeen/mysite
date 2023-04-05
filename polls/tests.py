from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from .models import Question, Choice
from django.urls import reverse


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


def create_qu(qu_text, days):
    time = timezone.now() + timedelta(days=days)
    return Question.objects.create(qu_text=qu_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_qu(self):
        resp = self.client.get(reverse('polls:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'No polls are available')
        self.assertQuerysetEqual(resp.context['latest_qu_list'], [])
    
    def test_past_qu(self):
        qu = create_qu(qu_text='Past qu.', days=-30)
        resp = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(resp.context['latest_qu_list'], [qu])
    
    def test_future_qu(self):
        create_qu(qu_text='Future qu.', days=30)
        resp = self.client.get(reverse('polls:index'))
        self.assertContains(resp, 'No polls are available')
        self.assertQuerysetEqual(resp.context['latest_qu_list'], [])

    def test_futureandpast_qu(self):
        qu = create_qu(qu_text='Past qu', days=-30)
        create_qu(qu_text='Future qu', days=30)
        resp = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(resp.context['latest_qu_list'], [qu])

    def test_two_past_qus(self):
        qu1 = create_qu(qu_text='Past qu 1', days=-30)
        qu2 = create_qu(qu_text='Past qu 2', days=-20)
        resp = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(resp.context['latest_qu_list'], [qu2, qu1])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        fq = create_qu(qu_text='Future question', days=5)
        resp = self.client.get(reverse('polls:detail', args=(fq.id,)))
        self.assertEqual(resp.status_code, 404)

    def test_past_question(self):
        pq = create_qu(qu_text='Past qu', days=-5)
        resp = self.client.get(reverse('polls:detail', args=(pq.id,)))
        self.assertContains(resp, pq.qu_text)


class QuestionResultsViewTests(TestCase):
    def test_future_qu(self):
        fq = create_qu(qu_text='Future qu', days=5)
        Choice.objects.create(qu_id=fq.id, ch_text='Not much', votes=3)
        resp = self.client.get(reverse('polls:results', args=(fq.id,)))
        self.assertEqual(resp.status_code, 404)

    def test_past_qu(self):
        pq = create_qu(qu_text='Past qu', days=-5)
        ch = Choice.objects.create(qu_id=pq.id, ch_text='Good choice', votes=10)
        resp = self.client.get(reverse('polls:results', args=(pq.id,)))
        self.assertContains(resp, ch.ch_text)
