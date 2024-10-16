from django.urls import path
from . import views

urlpatterns = [
    path('', views.monument_list, name='monument_list'),
    path('transfer/<int:monument_id>/', views.transfer_monument, name='transfer_monument'),
    path('add-lot/', views.add_lot, name='add_lot'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete/<int:monument_id>/', views.delete_monument, name='delete_monument'),
]
