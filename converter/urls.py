# converter/urls.py

from django.urls import path
from .views import register, login_view, logout_view, dashboard, convert_text, history, home, delete_history, delete_selected_histories

urlpatterns = [
    path('', home, name='home'),  # Landing page at root URL
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('convert/', convert_text, name='convert_text'),
    path('history/', history, name='history'),
    path('delete_selected/', delete_selected_histories, name='delete_selected_histories'),
    path('delete_history/<int:pk>/', delete_history, name='delete_history'),  # Ensure this line is still present
]
