from rest_framework import serializers
from .models import Company, Employee
from dj_rest_auth.registration.serializers import RegisterSerializer
from validate_docbr import CNPJ, CPF
from rest_framework.authtoken.models import Token
import phonenumbers


class CompanyCustomRegistrationSerializer(RegisterSerializer):
    cnpj = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        extra_data = {
            'cnpj': self.validated_data.get('cnpj', ''),
            'phone': self.validated_data.get('phone', ''),
            'address': self.validated_data.get('address', ''),
        }
        data.update(extra_data)
        return data

    def validate_cnpj(self, value):
        cnpj_validator = CNPJ()
        cleaned_cnpj = ''.join(filter(str.isdigit, value))
        if not cnpj_validator.validate(cleaned_cnpj):
            raise serializers.ValidationError("CNPJ inválido.")
        return cnpj_validator.mask(cleaned_cnpj) 
    
    def validate_phone(self, value):
        try:
            parsed_phone = phonenumbers.parse(value, "BR")
            if not phonenumbers.is_valid_number(parsed_phone):
                raise serializers.ValidationError("Número de telefone inválido.")
            formatted_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.NATIONAL)
            return formatted_phone
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Número de telefone inválido.")

    

    def save(self, request):
        user = super().save(request)
        user.is_company = True
        user.save()
        company = Company(
            seller=user,
            cnpj=self.cleaned_data.get('cnpj'),
            phone=self.cleaned_data.get('phone'),
            address=self.cleaned_data.get('address')
        )
        company.save()
        return user

class EmployeeCustomRegistrationSerializer(RegisterSerializer):
    cpf = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    employee_company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        extra_data = {
            'cpf': self.validated_data.get('cpf', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone': self.validated_data.get('phone', ''),
            'employee_company': self.validated_data.get('employee_company', ''),
        }
        data.update(extra_data)
        return data

    def validate_cpf(self, value):
        cpf_validator = CPF()
        cleaned_cpf = ''.join(filter(str.isdigit, value))
        if not cpf_validator.validate(cleaned_cpf):
            raise serializers.ValidationError("CPF inválido.")
        return cpf_validator.mask(cleaned_cpf)
    
    def validate_phone(self, value):
        try:
            parsed_phone = phonenumbers.parse(value, "BR")
            if not phonenumbers.is_valid_number(parsed_phone):
                raise serializers.ValidationError("Número de telefone inválido.")
            formatted_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.NATIONAL)
            return formatted_phone
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Número de telefone inválido.")

    def save(self, request):
        user = super().save(request)
        user.is_employee = True
        user.save()
        employee = Employee(
            seller=user,
            cpf=self.cleaned_data.get('cpf'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            phone=self.cleaned_data.get('phone')
            
        )
        employee.save()
        return user
