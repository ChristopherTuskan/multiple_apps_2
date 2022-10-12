from django.shortcuts import render, HttpResponse

def index(reqeust):
    return HttpResponse('placeholder to display all the surveys created')

def new(reqeust):
    return HttpResponse('placeholder for users to add a new survey')
