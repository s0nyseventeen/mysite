from django.shortcuts import render
from django.http import HttpResponse, Http404
from pprint import pprint as pp
from .models import Question


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
        quest = Question.objects.get(pk=qu_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    # or
    # quest = get_object_or_404(Question, qu_text='Just added')

    return render(request, 'polls/detail.html', {'quest': quest})


def results(request, qu_id):
    print(f'{request=}\n{type(request)=}')
    pp(request.__dict__)
    return HttpResponse(f"You're looking at the results of question {qu_id}")


def vote(request, qu_id):
    print(f'{request=}\n{type(request)=}')
    pp(request.__dict__)
    return HttpResponse(f"You're looking on voting on question {qu_id}")
