from django.urls import path
from accounts import views
urlpatterns = [
    path('register/', views.CustomerRegistrationView.as_view(),name='customerregister'),
    path('login/', views.CustomerLoginView.as_view(),name='customerlogin'),

]
