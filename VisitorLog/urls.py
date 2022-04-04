from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='visitor_home'),
    path('visitor_dashboard/', views.visitor_dashboard, name='visitor_dashboard'),
    path('add_visitor/', views.add_visitor, name='add_visitor'),
    path('update_visitor_status/<int:visitor_id>', views.update_visitor_status, name='update_visitor_status'),
    path('delete_visitor/<int:visitor_id>', views.delete_visitor, name='delete_visitor'),
    path('update_status', views.update_status, name='update_status'),
]