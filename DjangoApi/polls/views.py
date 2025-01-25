from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return HttpResponse("this is the polls application")

def detail(request, question_id): 
    return HttpResponse("You're looking at a question %s" % question_id)


def results(request, question_id): 
    response = "you're looking at the results od question %s"
    return HttpResponse(response,question_id)

def vote(request, question_id):
    response = "your voting on question %s"
    return HttpResponse(response,question_id)
