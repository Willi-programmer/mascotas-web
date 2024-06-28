
from django.contrib import admin
from django.urls import path
from core import views as core_views

from django.conf import settings
from django.conf.urls.static import static
from bd_mascota import views as bd
from bd_mascota.views import BlogListView, BlogCreate, contactoCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', core_views.index),
    #path ('contact/',bd.contacto),
    path ('services/',bd.servicios),
    #path ('blog/',bd.blog),
    path ('portafolio/',bd.portafolio),
    path ('ingresar/',core_views.login),
    path ('registro_u/',core_views.registroU),
    #CRUD PARA LA TABLA POST
    path ('blog/',BlogListView.as_view(),name="ListarPoster"),
    path ('Crear/',BlogCreate.as_view(),name="CrearPoster"),
    path ('contacto/',contactoCreate.as_view(),name="CrearContacto"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)