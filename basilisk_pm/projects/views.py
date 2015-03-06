from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from projects.models import Project

# Create your views here.
@login_required
def index(request):
    template = loader.get_template('project-base.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@login_required
def detail(request,project_id):
    template = loader.get_template('project.html')
    context = RequestContext(request, {})
    context['project'] = get_object_or_404(Project,pk=project_id)
    return HttpResponse(template.render(context))

@login_required
def code(request,project_id):
    template = loader.get_template('project-code.html')
    context = RequestContext(request, {})
    context['project'] = get_object_or_404(Project,pk=project_id)
    return HttpResponse(template.render(context))

@login_required
def files(request,project_id):
    template = loader.get_template('project-files.html')
    context = RequestContext(request, {})
    context['project'] = get_object_or_404(Project,pk=project_id)
    return HttpResponse(template.render(context))

@login_required
def settings(request,project_id):
    template = loader.get_template('project-settings.html')
    context = RequestContext(request, {})
    context['project'] = get_object_or_404(Project,pk=project_id)
    return HttpResponse(template.render(context))

def plist(request):
    template = loader.get_template('project-list.html')
    context = RequestContext(request, {})
    context['project_list'] = Project.objects.all()
    return HttpResponse(template.render(context))
