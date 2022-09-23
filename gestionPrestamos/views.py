#from django.shortcuts import render
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gestionPrestamos.models import Libro
from django.http import JsonResponse

class LibroView(View):
    
    @method_decorator(csrf_exempt) #CSRF codificacion que permite traer datos desde la URL
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self,request,isbn=""):
        
        if len(isbn)>0:
            libro=list(Libro.objects.filter(Isbn=isbn).values())
            if len(libro)>0:
                datos={'Libro':libro}
            else:
                datos={'mensaje': "No se encontro el libro."}
        else:
            Libros=list(Libro.objects.values())
            if len(Libros)>0:
               datos={"mensaje":Libros}
            else:
               datos={"mensaje":"No se encontraron libros."}
               
        return JsonResponse(datos)
    
    def post(self,request):
        data=json.loads(request.body)
        libro=Libro(Isbn=data['Isbn'],titulo=data['titulo'],editorial=data['editorial'],autor=data['autor'],no_page=data['no_page'])
        libro.save()
        datos={'mensaje':'Libro registrado exitosamente'}
        return JsonResponse(datos)
    
    def put(self,request,isbn):
        data=json.loads(request.body)
        libro=list(Libro.objects.filter(Isbn=isbn).values())
        if len(libro)>0:
            lib=Libro.objects.get(Isbn=isbn)
            lib.titulo=data["titulo"]
            lib.editorial=data["editorial"]
            lib.autor=data["autor"]
            lib.no_page=data["no_page"]
            lib.save()
            mensaje={"mensaje":"Libro Actualizado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro el Libro."} 
            
        return JsonResponse(mensaje)
    
    def delete(self,request,isbn):
        libro=list(Libro.objects.filter(Isbn=isbn).values())
        if len(libro)>0:
            Libro.objects.filter(Isbn=isbn).delete()
            mensaje={"mensaje":"Libro eliminado exitosamente."}
        else:
            mensaje={"mensaje":"No se encontro el libro."}
        
        return JsonResponse(mensaje)
    
#tabla prestamos 


    