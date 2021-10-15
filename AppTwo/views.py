from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # my_dict = {"insert_me": "Hello iam from AppTwo/index.html!!"}
    # return render(request, "AppTwo/index.html", context=my_dict)
    return render(request, "AppTwo/index.html")
    