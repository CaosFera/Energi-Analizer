from django.db import models
from users.models import Employee
from django.contrib.gis.db import models

class CurrentData(models.Model):
    lifespan = models.PositiveIntegerField("Vida Útil (em horas)", default=0)  
    power = models.DecimalField("Potência (W)", max_digits=6, decimal_places=2)  
    voltage = models.DecimalField("Voltagem (V)", max_digits=6, decimal_places=2)  
    current = models.DecimalField("Corrente (A)", max_digits=6, decimal_places=2)    


class Location(models.Model):
    #latitude = models.DecimalField("Latitude", max_digits=9, decimal_places=6)
    #longitude = models.DecimalField("Longitude", max_digits=9, decimal_places=6)
    street = models.CharField("Rua", max_length=100, default="")
    district = models.CharField("Bairro", max_length=100, default="")
    city = models.CharField("Cidade", max_length=100, default="")
    point = models.PointField()
    
class Hub(models.Model):
    hub_location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='hub_locations')
    installation_date = models.DateField("Data de Instalação", blank=False, null=False)

class Post(models.Model):
    installation_date = models.DateField("Data de Instalação", blank=False, null=False)
    type_lamp = models.CharField("Tipo de Lâmpada", max_length=50)
    active = models.BooleanField("Ativo ?", default=True)
    post_location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='post_locations')
    current_data = models.ForeignKey(CurrentData, on_delete=models.PROTECT, related_name='current_datas')

class MaintenanceHistory(models.Model):
    date = models.DateField("Data de Manutenção", blank=False, null=False)
    description = models.TextField("Descrição", default="", blank=True)
    post = models.ForeignKey( Post, on_delete=models.PROTECT, related_name="posts")
    user = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="users")


   
   