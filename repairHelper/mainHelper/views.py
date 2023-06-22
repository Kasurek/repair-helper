from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Repair, SparePart
from .forms import RegisterForm, RepairForm, CustomerForm, SpareForm, DeviceForm, RepairEditForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def default(request):
    return render(request, 'mainHelper/default_start.html')

#logowanie potrzebne do wyswietlenia strony
@login_required(login_url='/login')
def home(request):
    repairs = Repair.objects.all()
    
    if request.method == "POST":
        repairId = request.POST.get("repairId")
        repair = Repair.objects.filter(id = repairId).first()
        repair.delete()
    
    return render(request, 'mainHelper/home.html', {'repairs':repairs})

@login_required(login_url='/login')
def showSpares(request):
    spares = SparePart.objects.all()
    
    if request.method == "POST":
        spareId = request.POST.get("spareId")
        addQuantity = request.POST.get("addQuantity")
        sparePart = SparePart.objects.filter(id = spareId).first()
        sparePart.quantity += int(addQuantity)
        sparePart.save()
        print(addQuantity)
        print(spareId)
    
    return render(request, 'mainHelper/show_spares.html', {'spares':spares})


# widok z formularzem do utworzenia uzytkownika
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {"form" : form})


# pokazanie szczegółów naprawy
def repairDetail(request, id):
    repair = Repair.objects.get(id = id)
    usedParts = []
    if request.method == 'POST':
        repairModel = request.POST.get('repairModel')
        spareId = request.POST.get('spareId')
        if repairModel:
            spares = SparePart.objects.filter(model = repairModel).all()
            # tutaj przesyla te dane
            # return redirect('addSpareToRepair', repairModel=repairModel)
            return render(request, 'mainHelper/add_spare_to_repair.html', {'spares':spares})
        # dodawanie danej czesci do naprawy
        elif spareId:
            sparePart = SparePart.objects.get(id = spareId)
            sparePart.quantity -= 1
            repair.spareParts.add(sparePart)
            sparePart.save()
            context = {
                'repair':repair,
                'usedParts':usedParts
            }
            return render(request, 'mainHelper/repair_detail.html', context)
        else:
            repair.status = 'Finished'
            repair.save()
            return redirect('/home')
    
    return render(request, 'mainHelper/repair_detail.html', {'repair': repair})

# edycja szczegółów naprawy
def repairEdit(request, id):
    repair = Repair.objects.get(id = id)

    if request.method == 'POST':
        form = RepairEditForm(request.POST, instance=repair)
        if form.is_valid():
            repair.status = "Ongoing"
            repair.save()
            form.save()
            return redirect('repair-detail', id=id)
    else:
        form = RepairEditForm(instance=repair)

    return render(request, 'mainHelper/repair_edit.html', {'form': form})

# widok do utworzenia nowej naprawy
@login_required(login_url='/login')
def createRepair(request):
    if request.method == 'POST':
        form = RepairForm(request.POST)
        # zapisanie danych jesli formularz jest prawidlowy
        if form.is_valid():
            repair = form.save(commit=False)
            repair.createdBy = request.user
            repair.status = 'New repair'
            repair.save()
            # utworzenie unikalnego ID naprawy na podstawie pola ID
            update_id = Repair.objects.get(id = repair.id)
            update_id.repairIdentification = f"PI{repair.id}"
            update_id.save()
            # przekierowanie uzytkownika na strone startowa
            return redirect('/home')
    else:
        form = RepairForm()
    
    return render(request, 'mainHelper/create_repair.html', {"form":form})

#dodawanie nowego klienta
@login_required(login_url='/login')
def createCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        # zapisanie danych jesli formularz jest prawidlowy
        if form.is_valid():
            customer = form.save()
            # przekierowanie uzytkownika na strone startowa
            return redirect('/home')
    else:
        form = CustomerForm()
    
    return render(request, 'mainHelper/create_customer.html', {"form":form})

#dodawanie nowego rodzaju urządzenia
@login_required(login_url='/login')
def addDeviceType(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        # zapisanie danych jesli formularz jest prawidlowy
        if form.is_valid():
            device = form.save()
            # przekierowanie uzytkownika na strone startowa
            return redirect('/home')
    else:
        form = DeviceForm()
    
    return render(request, 'mainHelper/add_device_type.html', {"form":form})

# dodawanie nowej czesci zamiennej
@login_required(login_url='/login')
def addSpare(request):
    if request.method == 'POST':
        form = SpareForm(request.POST)
        # zapisanie danych jesli formularz jest prawidlowy
        if form.is_valid():
            spare = form.save()
            # przekierowanie uzytkownika na strone startowa
            return redirect('/home')
    else:
        form = SpareForm()
    
    return render(request, 'mainHelper/add_spare.html', {"form":form})