from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    template = loader.get_template('project.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@login_required
def code(request):
    template = loader.get_template('project-code.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@login_required
def files(request):
    template = loader.get_template('project-files.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@login_required
def settings(request):
    template = loader.get_template('project-settings.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
