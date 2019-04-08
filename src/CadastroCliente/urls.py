from django.urls import path
from .views import (ClienteList,
                    ClienteCreate,
                    ClienteUpdate,
                    ClienteDelete,
                    ClienteDetail)

urlpatterns = [
    path('', ClienteList.as_view(), name='cliente_list'),
    path('create/', ClienteCreate.as_view(), name='cliente_create'),
    path('update/<int:pk>/', ClienteUpdate.as_view(), name='cliente_update'),
    path('delete/<int:pk>/', ClienteDelete.as_view(), name='cliente_delete'),
    path('detail/<int:pk>/', ClienteDetail.as_view(), name='cliente_detail'),
]
