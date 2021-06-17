from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bug




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bugs_index(request):
    bugs = Bug.objects.all()
    return render(request, 'bugs/index.html', {'bugs' : bugs})

def bugs_detail(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    return render(request, 'bugs/detail.html', { 'bug': bug})

#CBVs

class BugCreate(CreateView):
    model = Bug
    fields = '__all__'
    success_url = '/bugs/'

class BugUpdate(UpdateView):
    model = Bug
    fields = ['scientific', 'description', 'location']

class BugDelete(DeleteView):
    model = Bug
    success_url = '/bugs/'