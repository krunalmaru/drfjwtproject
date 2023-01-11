from django.urls import path
from accounts import views
urlpatterns = [
    path('register', views.CustomerRegistrationView.as_view(),name='customer'),
]
