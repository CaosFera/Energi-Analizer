import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        # Verificar campos obrigatórios
        if not username:
            raise ValidationError("O campo 'username' é obrigatório.")
        if not email:
            raise ValidationError("O campo 'email' é obrigatório.")
        if not password:
            raise ValidationError("O campo 'password' é obrigatório.")

        # Validação de e-mail
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("O email fornecido é inválido.")

        # Verificar se o username e email são únicos
        if User.objects.filter(username=username).exists():
            raise ValidationError("O nome de usuário já está em uso.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("O email já está em uso.")

        # Criação do usuário
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        # Mesmo processo de validação para o superusuário
        if not password:
            raise ValidationError("O campo 'password' é obrigatório.")
        if not email:
            raise ValidationError("O campo 'email' é obrigatório.")
        if not username:
            raise ValidationError("O campo 'username' é obrigatório.")
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Nome de Usuário", db_index=True, max_length=255) 
    email = models.EmailField("E-mail", db_index=True, unique=True)
    is_active = models.BooleanField("Ativo ?", default=True)
    is_superuser = models.BooleanField("Super Usuário?", default=False)
    is_staff = models.BooleanField("Super Usuário?", default=False)
    is_company = models.BooleanField("Empresa?", default=False)
    is_employee = models.BooleanField("Funcionário?", default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    groups = models.ManyToManyField('auth.Group',  related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return f"{self.email}"
    
    def get_full_name(self):
        if isinstance(self, Company):
            return self.username
        elif isinstance(self, Employee):
            return f"{self.first_name} {self.last_name}"
        return self.username 

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email'),
            models.UniqueConstraint(fields=['username'], name='unique_username')
        ]
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]




class AbstractProfile(models.Model):
    photo = models.ImageField("Foto", upload_to="imagens/", blank=True, null=True)
    description = models.TextField("Descrição", default="")

    class Meta:
        abstract = True
        verbose_name = "Perfil Abstrato"
        verbose_name_plural = "Perfis Abstratos"


class Company(models.Model):   
    seller = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE)
    cnpj = models.CharField("CNPJ", max_length=18, blank=True, unique=True, null=True) 
    address = models.CharField("Endereço", max_length=250, blank=True, null=True, default="") 
    phone = models.CharField("Telefone", max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.seller.is_employee:
            raise ValidationError("O usuário não pode ser Empresa e Funcionário ao mesmo tempo.")
        self.seller.is_company = True
        self.seller.save(update_fields=['is_company'])
        super().save(*args, **kwargs)
   
    def name(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


    
class ProfileCompany(AbstractProfile):
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name="profile")

    class Meta:
        verbose_name = "Perfil de Empresa"
        verbose_name_plural = "Perfis de Empresas"



@receiver(post_save, sender=Company)
def create_company_profile(sender, instance, created, **kwargs):
    if created:
        ProfileCompany.objects.create(company=instance)

    
class Employee(models.Model):
    seller = models.OneToOneField(User, related_name='employee_seller', on_delete=models.CASCADE)
    position = models.CharField("Cargo", max_length=100, blank=True, null=True, default="")
    cpf = models.CharField("CPF", max_length=14, blank=True, unique=True,  null=True, default="")
    first_name = models.CharField("Nome", max_length=100, blank=True, null=True, default="")
    last_name = models.CharField("Sobrenome", max_length=100, blank=True, null=True, default="")
    phone = models.CharField("Telefone", max_length=15, blank=True, null=True)
    employee_company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="employees")   

    def save(self, *args, **kwargs):
        if self.seller.is_company:
            raise ValidationError("O usuário não pode ser Empresa e Funcionário ao mesmo tempo.")
        self.seller.is_employee = True
        self.seller.save(update_fields=['is_employee'])
        super().save(*args, **kwargs)


    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    
class ProfileEmployee(AbstractProfile):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="profile")

    class Meta:
        verbose_name = "Perfil de Funcionário"
        verbose_name_plural = "Perfis de Funcionários"


@receiver(post_save, sender=Employee)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        ProfileEmployee.objects.create(employee=instance)
    

