from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class AllModelView(ListView):
    template_name = 'index.html'
    models = AboutMyself
    queryset = AboutMyself.objects.all()[:1]
    # context_object_name = 'aboutMyself'
    def get_context_data(self, **kwargs):
        context = super( AllModelView, self ).get_context_data( **kwargs )
        # context['aboutMyself'] = AboutMyself.objects.all()
        context['myProjects'] = MyProject.objects.all()
        context['workExperiences'] = WorkExperience.objects.all()
        context['skills'] = Skill.objects.all()
        context['educations'] = Education.objects.all()
        context['languages'] = Language.objects.all()
        return context
