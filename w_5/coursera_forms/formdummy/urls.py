from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.FormDummyView.as_view()),

]
