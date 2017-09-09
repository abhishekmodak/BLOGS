# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from blogs.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse


def index(request):
        return render_to_response('blogs/index.html', {
        'posts': Blog.objects.all().order_by('-added_date')
    })



