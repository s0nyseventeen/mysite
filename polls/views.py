from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from pprint import pprint as pp
from .models import Question, Choice
from django.urls import reverse


def index(request):
    print(f'{request=}\n{type(request)=}')
    pp(request.__dict__)
    latest_qu_list = Question.objects.order_by('-pub_date')[:5]
#    templ = loader.get_template('polls/index.html')
    context = {'latest_qu_list': latest_qu_list}
#    return HttpResponse(', '.join([q.qu_text for q in latest_qu_list]))
#    return HttpResponse(templ.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, qu_id):
    print(f'{request=}\n{type(request)=}')
    pp(request.__dict__)

    try:
        qu = Question.objects.get(pk=qu_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    # or
    # qu = get_object_or_404(Question, qu_text='Just added')

    return render(request, 'polls/detail.html', {'qu': qu})


def results(request, qu_id):
    print(f'{request=}\n{type(request)=}')
    pp(request.__dict__)

    try:
        qu = Question.objects.get(id=qu_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    return render(request, 'polls/results.html', {'qu': qu})


def vote(request, qu_id: int):
    print(f'{request=}\n{type(request)=}')
    pp(request.__dict__)
    
    try:
        qu = Question.objects.get(id=qu_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    try:
        pp(f'{request.POST=}')
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
