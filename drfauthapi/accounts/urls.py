from django.urls import path
from accounts import views
urlpatterns = [
    path('register/', views.CustomerRegistrationView.as_view(),name='customerregister'),
    path('login/', views.CustomerLoginView.as_view(),name='customerlogin'),
    path('profile/', views.CustomerProfileView.as_view(), name='Customerprofile'),
    path('changepassword/', views.CustomerChangePasswordView.as_view(),name='passwordchange'),

]
