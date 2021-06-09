#coding: utf-8
from django.http import HttpResponse


def index_vews():
    return HttpResponse('hello git')