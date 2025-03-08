from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Questions, Choice
from django.urls import reverse
from django.db.models import F 


# Create your views here.
def index(request) :
    latest_question_list = Questions.objects.order_by("pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id): 
    try: 
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesnotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question":question})
        


def results(request, question_id): 
    response = "you're looking at the results of question %s"
    return HttpResponse(response,question_id)

def vote(request, question_id):
    response = "your voting on question %s"
    return HttpResponse(response,question_id)
