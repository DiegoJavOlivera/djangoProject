
from django.http import HttpResponse, JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("indexpage")

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse('about')


def project(request):
    projects = list( Project.objects.values())
    return JsonResponse(projects, safe = False)

def tasks(request,title):
    task = Task.objects.get(title=title)
    return HttpResponse('tasks: %s' % task.title)