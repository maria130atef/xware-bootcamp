from django.shortcuts import render
from django.http import HttpResponse
from django.template  import loader

# def try_hello(request):
#     template=loader.get_template("index.html")
#     return HttpResponse(template.render())


def try_hello(request):
     template=loader.get_template("parse firstname.html")
     dictsionary ={
          'firstname' :'Maria Atef'
     }
     return HttpResponse(template.render(context=dictsionary))




# def try_hello (request):
#     return HttpResponse("hello World")


# Create your views here.
