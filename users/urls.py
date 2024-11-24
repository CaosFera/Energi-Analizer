

from django.urls import path
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView
from users.serializers import EmployeeCustomRegistrationSerializer, CompanyCustomRegistrationSerializer

urlpatterns = [
    
        path('login/', LoginView.as_view(), name='rest_login'),
        path('logout/', LogoutView.as_view(), name='rest_logout'),  
        path('register/company/', RegisterView.as_view(serializer_class=CompanyCustomRegistrationSerializer), name='custom_register_company'),
        path('register/employee/', RegisterView.as_view(serializer_class=EmployeeCustomRegistrationSerializer), name='custom_register_employee'),
      
]

