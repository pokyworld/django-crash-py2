# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')