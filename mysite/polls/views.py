from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, request
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    # version 1 : Affiche un texte simple
    #return HttpResponse("Hello, world. You're at the polls index.")

    # version 2 : Affiche le contenu de la base de données
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    
    # version 3 : Utilise un template
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {'latest_question_list': latest_question_list}
    #page = template.render(context, request)
    #return HttpResponse(page)

    # version 4 : Avec raccourcit render
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # version 1
    #response = "You're looking at question {0}.".format(question_id)
    #return HttpResponse(response)

    # version 2
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})

    # version 3 : avec raccourci get or 404
    question = get_object_or_404(Question, pk=question_id) 
    return render(request, 'polls/detail.html', {'question': question})




def results(request, question_id):
    response = "You're looking at the results of question {0}.".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    response = "You're voting on question {0}.".format(question_id)
    return HttpResponse(response)
