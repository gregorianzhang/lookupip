# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#from yoyo.app.login.models import *

def index(request):
    #return render_to_response("account_base.html")
    #return HttpResponse("<html>Test page</html>")
    return HttpResponse("<html><body>Test page </body></html>")


