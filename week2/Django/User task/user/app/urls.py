from django.urls import path
# from . import views
from app.views import  hello,home,info

urlpatterns = [
    # path('app/', views.app, name='app'),
    path('hello/',hello),
    path('home/', home),
    path('info/',info)


]
