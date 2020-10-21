from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete,
    HoraExtraNovo
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_horaextra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='update_horaextra'),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name='delete_horaextra'),
    path('novo/', HoraExtraNovo.as_view(), name='create_horaextra'),

]
