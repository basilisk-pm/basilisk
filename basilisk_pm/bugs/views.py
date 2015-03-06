from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from projects.models import Project

# Create your views here.
@login_required
def index(request,project_id):
    template = loader.get_template('bugs.html')
    context = RequestContext(request, {})
    context['project'] = get_object_or_404(Project,pk=project_id)
    return HttpResponse(template.render(context))

@login_required
def new_issue(request,project_id):
    template = loader.get_template('bugs-new.html')
    context = RequestContext(request, {})
    context['project'] = get_object_or_404(Project,pk=project_id)
    return HttpResponse(template.render(context))

@login_required
def all_issues(request,project_id):
    template = loader.get_template('bugs-list.html')
    context = RequestContext(request, {})
    context['project'] = get_object_or_404(Project,pk=project_id)
    return HttpResponse(template.render(context))
