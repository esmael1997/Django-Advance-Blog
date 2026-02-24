from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    #path('cbv_index', views.IndexView.as_view(), name="cbv_index"),
    #path('go-to-maktabkhooneh', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),
    path('post/', views.PostListView.as_view(),name='post_list'),
]