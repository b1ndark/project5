from django.urls import path
from . import views


urlpatterns = [
    path('<int:about_id>/', views.about, name='about'),
]