from django.urls import path
from .views import *
urlpatterns=[
path('create/',create_view),
path('list/',list_view,name='list'),
path('<id>/detail',detail_view),
path('<id>/update',update_view),
path('<id>/delete',delete_view),
]
