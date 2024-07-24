from django.shortcuts import render

from django.http import HttpResponse

from django.template  import loader

def hello(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())

def home(request):
    template=loader.get_template("home.html")
    return HttpResponse(template.render())

def info(request):
    template=loader.get_template("info.html")
    dic={"name":"maria","age":20 ,"grade":6}
    return HttpResponse(template.render(context=dic))

# Create your views here.
