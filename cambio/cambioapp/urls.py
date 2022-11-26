from django.urls import path
from .views import cambios_list_view


urlpatterns = [
    path('cambios', cambios_list_view, name='cambios-list'),
]
 