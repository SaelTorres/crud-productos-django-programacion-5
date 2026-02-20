from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto_list'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('producto/nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('producto/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),
]
