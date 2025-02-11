from . import views
from django.urls import path


urlpatterns = [
    path('registro/', views.Signup.as_view(), name='Signup'),

]
