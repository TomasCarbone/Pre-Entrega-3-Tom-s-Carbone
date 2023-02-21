
from django.urls import path
from AppSnake import views

urlpatterns= [
            path('',views.inicio,name= 'Inicio'),
            path('vendedores/', views.vendedor,name='Vendedores'),
            path('compradores/',views.comprador,name="Comprador"),
            path('auto/',views.auto, name='Auto'),
            path('compradorFormulario/',views.compradorFormulario, name='compradorFormulario'),
            path('compradorBusqueda/',views.compradorBusqueda, name='compradorBusqueda'),
            path('buscar/',views.buscar),
            path('vendedorFormulario/',views.VendedorFormulario,name='vendedorFormulario'),
            path('vendedorBusqueda/',views.vendedorBusqueda,name='vendedorBusqueda'),
            path('buscar2/',views.buscar2),
            
            ]