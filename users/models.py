import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404
from EnergiAnalizer.abstract.models import AbstractModel, AbstractManager
from validate_docbr import CPF, CNPJ
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class UserManager(BaseUserManager, AbstractManager):
    def create_user(self, username, email, password=None, **kwargs):    
        if username is None:
            raise TypeError('Os usuários devem ter um nome de usuário.')
        if email is None:
            raise TypeError('Os usuários devem ter um email.')
        if password is None:
            raise TypeError('O usuário deve ter uma senha.')
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        if password is None:
            raise TypeError('Os superusuários devem ter uma senha.')
        if email is None:
            raise TypeError('Os superusuários devem ter um email.')
        if username is None:
            raise TypeError('Os superusuários devem ter um nome de usuário.')
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Nome de Usuário", db_index=True, max_length=255, unique=True) 
    email = models.EmailField("E-mail", db_index=True, unique=True)
    is_active = models.BooleanField("Ativo ?", default=True)
    is_superuser = models.BooleanField("Super Usuário?", default=False)
    is_staff = models.BooleanField("Super Usuário?", default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email']
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
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]


phone_validator = RegexValidator(regex=r'^\(\d{2}\) \d{4,5}-\d{4}$', message="Número de telefone inválido.")
cnpj_validator = RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', message="CNPJ inválido. O formato deve ser XX.XXX.XXX/0001-XX.")
cpf_validator = RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message="CPF inválido. O formato deve ser XXX.XXX.XXX-XX.")



class AbstractProfile(models.Model):
    photo = models.ImageField("Foto", upload_to="imagens/", blank=True, null=True)
    description = models.TextField("Descrição", default="")

    class Meta:
        abstract = True

class Company(User):   
    cnpj = models.CharField("CNPJ", max_length=18, blank=True, unique=True, null=True, default="", validators=[cnpj_validator]) 
    address = models.CharField("Endereço", max_length=250, blank=True, null=True, default="") 
    phone = models.CharField("Telefone", max_length=15, validators=[phone_validator], blank=True, null=True)

    def clean(self):
        super().clean()
        cnpj_validator = CNPJ()
        if self.cnpj and not cnpj_validator.validate(self.cnpj):
            raise ValidationError("CNPJ inválido.")
   
    def name(self):
        return f"{self.username}"
    
class ProfileCompany(AbstractProfile):
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name="profile")


@receiver(post_save, sender=Company)
def create_company_profile(sender, instance, created, **kwargs):
    if created:
        ProfileCompany.objects.create(company=instance)

    
class Employee(User):
    position = models.CharField("Cargo", max_length=100, blank=True, null=True, default="")
    cpf = models.CharField("CPF", max_length=14, blank=True, unique=True,  null=True, default="", validators=[cpf_validator])
    first_name = models.CharField("Nome", max_length=100, blank=True, null=True, default="")
    last_name = models.CharField("Sobrenome", max_length=100, blank=True, null=True, default="")
    phone = models.CharField("Telefone", max_length=15, validators=[phone_validator], blank=True, null=True)
    employee_company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="employees")

    def clean(self):
        super().clean()
        cpf_validator = CPF()
        if self.cpf and not cpf_validator.validate(self.cpf):
            raise ValidationError("CPF inválido.")
        
    

    def name(self):
        return f"{self.first_name} {self.last_name}"
    
class ProfileEmployee(AbstractProfile):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="profile")

@receiver(post_save, sender=Employee)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        ProfileEmployee.objects.create(employee=instance)
    

