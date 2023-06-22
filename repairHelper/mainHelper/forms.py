from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Repair, Customer, SparePart, DeviceType, Employee
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Employee
        fields = ["username", "email", "password1", "password2", "position"]
        
class RepairForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Choose the customer')
    deviceType = forms.ModelChoiceField(queryset=DeviceType.objects.all(), label='Type of device')
    class Meta:
        model = Repair
        fields = ['problemInfo', 'deviceType', 'repairModel', 'customer']
        
class RepairEditForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Choose the customer')
    deviceType = forms.ModelChoiceField(queryset=DeviceType.objects.all(), label='Type of device')
    class Meta:
        model = Repair
        fields = ['problemInfo', 'repairInfo', 'deviceType', 'repairModel', 'customer']
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstName','lastName', 'emailAddress']
        
class SpareForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['nameOfPart','model', 'quantity']
        
class DeviceForm(forms.ModelForm):
    class Meta:
        model = DeviceType
        fields = ['devicetype']