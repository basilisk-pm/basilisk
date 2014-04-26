from django.shortcuts import render
from django.http import HttpResponse
from code_viewer.models import Repo

# Create your views here.
def index(request):
    repo_list = Repo.objects.all().order_by('-repo_name')[:1]
    context = {'repo_list': repo_list}
    return render(request, 'code_viewer/index.html', context)


