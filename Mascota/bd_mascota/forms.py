from django import forms
from .models import Post, contacto

class BlogForms(forms.ModelForm):
    
    class Meta:
        model=Post
        
        fields= "__all__"
        #fields = ["imagen"]
        
class contactoForms(forms.ModelForm):
    
    class Meta:
        model= contacto
        
        fields= "__all__"        