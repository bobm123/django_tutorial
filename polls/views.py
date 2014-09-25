from django.http import Http404
from django.shortcuts import render
#from django.http import HttpResponse


from polls.models import Question

# first version just delivers some static text. This is about where
# the first couple chapters of TDD were in their django app
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404
    else:
        context = {'question': question}
        return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

