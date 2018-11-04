from django.shortcuts import render
from django.views.generic import View
from django.views.generic import View,TemplateView,ListView,DateDetailView
from django.http import HttpResponse
from . import models

# Create your views here.
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class Based View")

class IndexView(TemplateView):
    template_name = 'index.html'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['inject'] = 'Basic Injection!'
#         return context

class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School

class SchoolDetailView(DateDetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = 'CBV_app/school_details.html'