from django.urls.conf import path
from AppBebidas.views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
]
