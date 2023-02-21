from django.shortcuts import render
from django.http import HttpResponse
from AppSnake.models import *

#from django.http import HttpResponse
from AppSnake.forms import form_vendedor,form_comprador
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def inicio(request):
    
    return render(request,'AppSnake/Inicio.html')


def comprador(request):
    comprador= Comprador.objects.all()
    contexto= {"comprador":Comprador}
    return render(request,'AppSnake/compradores.html',contexto) 

def auto(request):

    return render(request,'AppSnake/Auto.html')

def compradorFormulario(request):
    if request.method == "POST":
        miFormulario=form_comprador(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            compradores= Comprador(nombre=informacion['nombre'],apellido= informacion['apellido'], auto=informacion['auto'], oferta= informacion['oferta'])
            compradores.save()
            return render(request,'AppSnake/inicio.html') 
    else:
        miFormulario=form_comprador()
    return render(request,'AppSnake/compradorFormulario.html',{'miFormulario':miFormulario})

def compradorBusqueda(request):
    return render(request,'AppSnake/compradorBusqueda.html',{"comprador":Comprador})

def buscar(request):
    if request.GET["auto"]:

        auto=request.GET["auto"]
        comprador=Comprador.objects.filter(credencial__icontains=auto)

        return render(request,"AppSnake/resultadoBusqueda.html",{"comprador":comprador,"auto":auto})
    else:
        respuesta='No enviaste datos'
       
    return HttpResponse(respuesta)

def vendedor(request):
    vendedores= Vendedor.objects.all()
    contexto= {"vendedores":vendedores}
    return render(request,'AppSnake/vendedores.html',contexto)
 
def VendedorFormulario(request):
    if request.method == "POST":
        miFormulario=form_vendedor(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            vendedores= Vendedor(nombre=informacion['nombre'],apellido= informacion['apellido'], modelo=informacion['modelo'], kilometros= informacion['kilometros'])
            vendedores.save()
            return render(request,'AppSnake/inicio.html') 
    else:
        miFormulario=form_vendedor()
    return render(request,'AppSnake/vendedorFormulario.html',{'miFormulario':miFormulario})

def vendedorBusqueda(request):
    return render(request,'AppSnake/vendedorBusqueda.html',{"vendedor":Vendedor})

def buscar2(request):
    if request.GET["modelo"]:

        modelo=request.GET["modelo"]
        vendedores=Vendedor.objects.filter(modelo__icontains=modelo)

        return render(request,"AppSnake/resultadoBusqueda2.html",{"vendedores":vendedores,"modelo":modelo})
    else:
        respuesta='No enviaste datos'
       
    return HttpResponse(respuesta)