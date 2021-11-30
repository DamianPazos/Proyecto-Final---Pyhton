from django.urls.conf import path
from AppBebidas.views import inicio, lista_cervezas, lista_gaseosas, lista_vinos, nueva_cerveza

urlpatterns = [
    path('', inicio, name='inicio'),
    path('listaCervezas/', lista_cervezas , name='listaCervezas'),
    path('listaGaseosas/', lista_gaseosas , name='listaGaseosas'),
    path('listaVinos/', lista_vinos , name='listaVinos'),
    path('listaCervezas/nueva', nueva_cerveza, name='nuevaCerveza'),
]
