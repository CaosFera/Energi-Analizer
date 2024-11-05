from django.urls import path
from .views import CompanyRegistrationView, EmployeeRegistrationView
from dj_rest_auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/company/', CompanyRegistrationView.as_view(), name='company-register'),
    path('register/employee/', EmployeeRegistrationView.as_view(), name='employee-register'),
    path('api/v1/login/', LoginView.as_view(), name='rest_login'),
    path('api/v1/logout/', LogoutView.as_view(), name='rest_logout'),
]



