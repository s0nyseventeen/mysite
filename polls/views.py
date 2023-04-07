from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from pprint import pprint as pp

# func views

def index(request):
    latest_qu_list = Question.objects.order_by('-pub_date')[:5]
#    templ = loader.get_template('polls/index.html')
    context = {'latest_qu_list': latest_qu_list}
#    return HttpResponse(', '.join([q.qu_text for q in latest_qu_list]))
#    return HttpResponse(templ.render(context, request))
    return render(request, 'polls/index.html', context)
#
#
#def detail(request, qu_id):
#    try:
#        qu = Question.objects.get(pk=qu_id)
#    except Question.DoesNotExist:
#        raise Http404('Question does not exist')
#
#    # or
#    # qu = get_object_or_404(Question, qu_text='Just added')
#
#    return render(request, 'polls/detail.html', {'qu': qu})
#
#
#def results(request, qu_id):
#    try:
#        qu = Question.objects.get(id=qu_id)
#    except Question.DoesNotExist:
#        raise Http404('Question does not exist')
#
#    return render(request, 'polls/results.html', {'qu': qu})


def vote(request, qu_id: int):
    try:
        qu = Question.objects.get(id=qu_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    try:
        selected_ch = qu.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the qu voting form
        return render(
            request,
            'polls/detail.html',
            {'qu': qu, 'error_message': "You didn't select a choice"}
        )
    else:
        selected_ch.votes += 1
        selected_ch.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back btn
        return HttpResponseRedirect(reverse('polls:results', args=(qu.id, )))


# class views

#class IndexView(generic.ListView):
#    template_name = 'polls/index.html'
#    context_object_name = 'latest_qu_list'
#
#    pp(f'{generic.ListView.__dict__=}')
#    pp(f'{dir(generic.ListView)=}')
#
#    def get_queryset(self):
#        return Question.objects.filter(
#            pub_date__lte=timezone.now()
#        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
