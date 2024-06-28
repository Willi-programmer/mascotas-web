from django.shortcuts import render
from .models import Post, contacto, Servicio, Producto
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import BlogForms, contactoForms




"""def blog(request):
    post=Post.objects.all()
    return render(request, "bd_mascota/blog.html",{"blog":post})"""


#CBD EN LA CRUD: LISTVIEW - POST Y CATEGORIA DEL TEMPLATE BLOG
class BlogListView(ListView):
    model=Post
    paginate_by=1

    
    def get_queryset(self):
        return Post.objects.all()
    
    #ENVIA IMNFORMACIOON ADICIONAL LA CUAL SIRVE PARA PODER PAGINAR
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    #CBD EN LA CRUD: CREATEVIEWS - POST Y CATEGORIA DEL TEMPLATE BLOG
class BlogCreate(CreateView):
    model = Post #tabla
    form_class = BlogForms #formulario creado en  el forms.py
    template_name = "bd_mascota/CreateBlog.html" #pagina html donde esta el formulario
    success_url = reverse_lazy("CrearPoster") #nombre que se le da en la url(name="CrearPoster")



class contactoCreate(CreateView):
    model = contacto
    form_class = contactoForms #formulario creado en  el forms.py
    template_name = "bd_mascota/contact.html" #pagina html donde esta el formulario
    success_url = reverse_lazy("CrearContacto") #nombre que se le da en la url(name="CrearContacto"),para que cargue la BD

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "bd_mascota/services.html", {"servicios":servicios})

def portafolio(request):
    producto=Producto.objects.all()
    return render(request, "bd_mascota/portafolio.html", {"productos":producto})

