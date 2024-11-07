from django.urls import path
#
from . import views

app_name = "home_app"
urlpatterns = [
    path(
        'home/', 
        views.HomePage.as_view(),
        name = 'panel'),
    path(
        'mixin/', 
        views.TemplatePrueba.as_view(),
        name = 'mixin'),
]
