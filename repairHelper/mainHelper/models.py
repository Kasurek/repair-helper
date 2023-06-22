from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Employee(AbstractUser):
    CHOOSE_POSITION = (
        ('warehouse', 'Warehouse'),
        ('service', 'Service')
    )
    position = models.CharField(max_length=50, choices=CHOOSE_POSITION)
    
class Customer(models.Model):
    firstName = models.CharField('Imie', max_length=200)
    lastName = models.CharField('Nazwisko', max_length=200)
    emailAddress = models.CharField('Adres email', max_length=200)
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName   
    
class DeviceType(models.Model):
    devicetype = models.CharField('Type of device', max_length=200)
    
    def __str__(self):
        return self.devicetype
    

class SparePart(models.Model):
    nameOfPart = models.CharField('Name of part',max_length=200)
    quantity = models.IntegerField('Quantity')
    model = models.CharField('Device model', max_length=200)
    
    def __str__(self):
        return self.nameOfPart

class Repair(models.Model):
    repairIdentification = models.CharField('Repair ID', max_length=200)
    repairInfo = models.TextField('Diagnose and repair',max_length=500)
    problemInfo = models.TextField('Informations about the problem', max_length=500)
    repairModel = models.CharField('Model of device', max_length=200)
    status = models.CharField('Status', max_length=200)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    deviceType = models.ForeignKey(DeviceType, blank=True, null=True, on_delete=models.CASCADE)
    createdBy = models.CharField('Creater by', max_length=200)
    startDate = models.DateField('Start of repair', auto_now_add=True)
    lastUpdate = models.DateField('End of repair', auto_now=True)
    spareParts = models.ManyToManyField(SparePart, blank=True)
    
    def __str__(self):
        return self.repairIdentification
    
    def get_start_date(self):
        return self.startDate.strftime('%d-%m-%Y')
    
    def get_last_update(self):
        return self.lastUpdate.strftime('%d-%m-%Y')
    
    
    

    
    
    

    
