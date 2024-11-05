from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from users.serializers import EmployeeCustomRegistrationSerializer, CompanyCustomRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
    

class CompanyRegistrationView(RegisterView):
    serializer_class = CompanyCustomRegistrationSerializer


class EmployeeRegistrationView(RegisterView):
    serializer_class = EmployeeCustomRegistrationSerializer


class EmployeeRegistrationView(RegisterView):
    serializer_class = EmployeeCustomRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assumindo que o usuário autenticado é uma empresa
        user = self.request.user
        if not user.is_company:
            raise serializers.ValidationError("Apenas empresas podem adicionar funcionários.")

        # Passa o `employee_company` automaticamente para o serializer
        serializer.save(employee_company=user.company)
