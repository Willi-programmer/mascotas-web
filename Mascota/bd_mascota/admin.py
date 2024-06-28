from django.contrib import admin

from .models import Mascota, MascotaServicio, Producto, ProductoUsuario, Servicio, Usuario, Post, Categoria, contacto

class MascotaAdmin(admin.ModelAdmin):
    list_display = ("id_mas","tipo_mas", "raza","nom_mas","fecha_nac","foto","id_usuario")
admin.site.register(Mascota,MascotaAdmin)

class MascotaServicioAdmin(admin.ModelAdmin):
    list_display = ("codigo","id_servicio", "id_mas","fecha_servicio")
admin.site.register(MascotaServicio,MascotaServicioAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id_pro","nom_pro", "desc_pro","precio_pro","foto_pro","stock_pro")
admin.site.register(Producto, ProductoAdmin)

class ProductoUsuarioAdmin(admin.ModelAdmin):
    list_display = ("codpu","id_persona", "id_pro","cant","total")
admin.site.register(ProductoUsuario, ProductoUsuarioAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ("id_serv","nom","descripcion","precio","imagen")
admin.site.register(Servicio,ServicioAdmin)

class UsuariotaAdmin(admin.ModelAdmin):
    list_display = ("id_persona","usuario","pass_field","nom","ape","dir","tel","tel","correo","tipo","foto")
admin.site.register(Usuario,UsuariotaAdmin)


#CLASES PARA EL BLOG
class BlogAdmin(admin.ModelAdmin):
    #DESPLEGA LOS DATOS DE LAS TABLA
    list_display=("titulo","contenido","fecha","imagen","Fcreacion","Fedicion")
    ordering=("titulo","fecha")
    list_filter=("id_persona_id__nom","titulo")
    
admin.site.register(Post,BlogAdmin) 


class CategoriaAdmin(admin.ModelAdmin):
    #DESPLEGA LOS DATOS DE LAS TABLA
    list_display=("nom","FCreacion")
    
admin.site.register(Categoria,CategoriaAdmin) 

class contactoAdmin(admin.ModelAdmin):
    
    #DESPLEGA LOS DATOS DE LA TABLA
    list_display = ("codigo","nombre","correo","tipo_consulta","mensaje","avisos")
    
admin.site.register(contacto,contactoAdmin) 


