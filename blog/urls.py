from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path('cbv_index', views.indexView.as_view(), name="cbv_index"),
    path('go-to-index', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),
]