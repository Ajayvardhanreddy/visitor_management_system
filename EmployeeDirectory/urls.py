from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='emp_home'),
    path('emp_dashboard/', views.emp_dashboard, name='emp_dashboard'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('update/<int:emp_id>', views.update, name='update'),
    path('update_emp_details/', views.update_emp_details, name='update_emp_details'),
    path('delete_emp/<int:emp_id>', views.delete_emp, name='delete_emp'),
    path('api_emp/', views.Emp.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]