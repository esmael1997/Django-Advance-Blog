from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView
from .models import Post
from django.shortcuts import get_object_or_404

#class IndexView(TemplateView):
#'''
#a class based view to show index page
#'''
    #template_name = 'index.html'
    
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context["name"] = "Esmael"
        #context["posts"] = Post.objects.all()
         
        #return context
    
#class RedirectToMaktab(RedirectView):
    #url = 'https://maktabkhooneh.com'
    
    #def get_redirect_url(self, *args, **kwargs):
        #Post = get_object_or_404(Post, pk-kwargs['pk'])
        #print(post)
        #article.update_counter()
        #return super().get_redirect_url(*args, **kwargs)
        
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
        
