from django.urls import path, include
from django.views.generic import TemplateView
from .views import APIDataView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('get_stat/', APIDataView.as_view()),
]
