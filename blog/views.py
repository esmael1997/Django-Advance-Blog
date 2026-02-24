from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post

class IndexView(TemplateView):
    '''
    a class based view to show index page
    '''
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Esmael"
        context["posts"] = Post.objects.all()
         
        return context
        
