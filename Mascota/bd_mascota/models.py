from django.db import models
from django.utils.timezone import now


roles_usuarios=[
    [0, "Administrador"],
    [1, "Cliente"]
]
tipo_mascota=[
    ["Perro", "Perro"],
    ["Gato", "Gato"],
    ["Ave", "Ave"],
    ["Reptil", "Reptil"],
    ["Roedores", "Roedores"],
    ["Conejo", "Conejo"],
]

class Mascota(models.Model):
    id_mas = models.IntegerField(primary_key=True)
    tipo_mas = models.CharField(max_length=45,choices=tipo_mascota)
    raza = models.CharField(max_length=45)
    nom_mas = models.CharField(max_length=45)
    fecha_nac = models.DateField()
    foto = models.ImageField(upload_to='mascotas/')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'mascota'
        
    def __str__(self):
        texto= "{0}"
        return texto.format(self.id_mas)    


class MascotaServicio(models.Model):
    codigo = models.AutoField(primary_key=True)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')
    id_mas = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='id_mas')
    fecha_servicio = models.DateField()

    class Meta:
        managed = False
        db_table = 'mascota_servicio'


class Producto(models.Model):
    id_pro = models.AutoField(primary_key=True)
    nom_pro = models.CharField(max_length=45)
    desc_pro = models.CharField(max_length=60)
    precio_pro = models.DecimalField(max_digits=10, decimal_places=3)
    foto_pro = models.ImageField(upload_to='producto/')
    stock_pro = models.FloatField()

    class Meta:
        managed = False
        db_table = 'producto'
        
    def __str__(self):
        texto= "{0}"
        return texto.format(self.id_pro)    


class ProductoUsuario(models.Model):
    codpu = models.AutoField(db_column='codPU', primary_key=True)  # Field name made lowercase.
    id_persona = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_persona')
    id_pro = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_pro')
    cant = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'producto_usuario'
        
        


class Servicio(models.Model):
    id_serv = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=70)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='servicio/')

    class Meta:
        managed = False
        db_table = 'servicio'
        
    def __str__(self):
        texto= "{0}"
        return texto.format(self.id_serv)    


class Usuario(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    usuario = models.CharField(unique=True, max_length=45, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=45, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    nom = models.CharField(max_length=45, blank=True, null=True)
    ape = models.CharField(max_length=45, blank=True, null=True)
    dir = models.CharField(max_length=45, blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True,choices=roles_usuarios)
    foto = models.ImageField(upload_to="BlogImg", null=True, blank=True, verbose_name="imagen")

    class Meta:
        managed = False
        db_table = 'usuario'
        
    def __str__(self):
        texto= "{0}"
        return texto.format(self.id_persona)    
    
    #ESTOS MODELOS IMPORTAMOS LA LIBRERI TIMEZONE
class Categoria(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nombre")
    FCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    
    class Meta:
        verbose_name="categoria"
    
    def __str__(self):
        texto="{0}"
        return texto.format(self.nom)


class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo")    
    contenido = models.TextField(verbose_name="Contenido")
    fecha = models.DateTimeField(default=now, verbose_name="Fech publicacion")
    imagen = models.ImageField(upload_to="BlogImg", null=True, blank=True, verbose_name="Imagen")   
    id_persona = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True)
    categorias =models.ManyToManyField(Categoria, verbose_name="Categorias")
    Fcreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    Fedicion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edicion")
    
    
    class Meta:
            verbose_name="Post"
        
    def __str__(self):
        texto="{0}"
        return texto.format(self.titulo) 
    
#ESTE ES EL MODELO PARA LOS CONTACTOS
opciones_consultas=[
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"],
]
class contacto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=45, blank=True, null=True)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
        
        
def __str__(self):
    return self.title
        

