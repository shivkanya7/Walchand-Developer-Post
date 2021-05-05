from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.homepage,name='hoempage'),
    path("login/<slug:slug>",views.login,name = 'login'),
    path("projects/",views.display_projects,name = 'display_projects'),
    path("projects/<int:id>/<slug:slug>",views.single_project,name = 'single_project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)