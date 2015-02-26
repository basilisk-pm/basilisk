from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    template = loader.get_template('bugs.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@login_required
def new_issue(request):
    template = loader.get_template('bugs-new.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@login_required
def all_issues(request):
    template = loader.get_template('bugs-list.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
