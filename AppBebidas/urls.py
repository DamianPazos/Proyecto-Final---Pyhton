from django.urls.conf import path
from AppBebidas.views import inicio, lista_cervezas, lista_gaseosas, lista_vinos, nueva_cerveza, nueva_gaseosa, nueva_vino


urlpatterns = [
    path('', inicio, name='inicio'),
    path('listaCervezas/', lista_cervezas , name='listaCervezas'),
    path('listaGaseosas/', lista_gaseosas , name='listaGaseosas'),
    path('listaVinos/', lista_vinos , name='listaVinos'),
    path('listaCervezas/nueva', nueva_cerveza, name='nuevaCerveza'),
    path('listaGaseosas/nueva', nueva_gaseosa , name='nuevaGaseosa'),
    path('listaVinos/nueva', nueva_vino , name='nuevaVino'),
    
]
