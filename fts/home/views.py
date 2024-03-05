from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .filters import CarFilter
from .forms import BrandForm, CarForm, ColourForm, OwnerRecordForm
from .models import Brand, Car, Colour, OwnerRecord

def create_brand(request):
    """ Create new brand """

    if request.method == 'GET':
        brd_form = BrandForm()
        return render(request, "addbrand.html", {'data':brd_form})
    else:
        brd_form = BrandForm(request.POST)
        if brd_form.is_valid():
            brd_form.save()
            messages.success(request, 'Brand added successfully!')
            return redirect(create_brand)
        else:
            return render(request, "addbrand.html", {'data':brd_form})

def view_brands(request):
    """ List all brands """

    brands = Brand.objects.all()
    brand_data = []

    for brand in brands:
        newcars = Car.objects.filter(brand=brand, condition='New').count()
        usedcars = Car.objects.filter(brand=brand, condition='Used').count()
        total_cars = newcars + usedcars
        brand_data.append({'name': brand, 'newcars': newcars, 'usedcars': usedcars, 'total_cars': total_cars})

    return render(request, 'viewbrands.html', {'data': brand_data})

def create_colour(request):
    """ Create new colour """

    if request.method == 'GET':
        clr_form = ColourForm()
        return render(request, "addcolour.html", {'data':clr_form})
    else:
        clr_form = ColourForm(request.POST)
        if clr_form.is_valid():
            clr_form.save()
            messages.success(request, 'Colour added successfully!')
            return redirect(create_colour)
        else:
            return render(request, "addcolour.html", {'data':clr_form})

def view_colours(request):
    """ List all colours """

    colours = Colour.objects.all()
    return render(request, "viewcolours.html", {'data':colours})

def create_car(request):
    """ Create new Car"""
    
    if request.method == 'GET':
        car_form = CarForm()
        return render(request, 'addcar.html', {'data': car_form})
    else:
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, 'Car added successfully!')
            return redirect(create_car)

def home(request):
    """View all cars"""

    car_list = Car.objects.all()
    car_filter = CarFilter(request.GET, queryset=car_list)
    paginator = Paginator(car_filter.qs, 10)

    page_number = request.GET.get('page')
    page_data = paginator.get_page(page_number)

    return render(request, 'home.html', {'filter': car_filter, 'data': page_data})

def edit_car(request, id):
    """Update a car"""

    carobj = get_object_or_404(Car, id=id)
    if request.method == 'GET':
        car_form = CarForm(instance=carobj)
        return render(request, "editcar.html", {'form': car_form, 'data': carobj})
    else:
        car_form = CarForm(request.POST, instance=carobj)
        if car_form.is_valid():
            car_form.save()
            messages.success(request, 'Car updated successfully!')
            return redirect(reverse('cardetails', kwargs={'id': id}))

def destroycar(request,id):
    """Delete a car """

    carobj = Car.objects.get(id=id)
    carobj.delete()
    messages.warning(request, 'Car deleted successfully!')
    return redirect(home)

def car_details(request, id):
    """Get car details"""

    car = get_object_or_404(Car, pk=id)
    own_rec = OwnerRecord.objects.filter(car=car)
    return render(request, 'car_details.html', {'car': car, 'own_rec': own_rec})

def add_owner(request, id):
    """Add owner record"""

    carobj = Car.objects.get(pk=id)
    if request.method == 'GET':
        carform = OwnerRecordForm()
        return render(request, 'addowner.html', {'form': carform, 'car': carobj})
    else:
        carform = OwnerRecordForm(request.POST)
        if carform.is_valid():
            owned_from = carform.cleaned_data.get('owned_from')
            owned_to = carform.cleaned_data.get('owned_to')

            overlapping_owners = OwnerRecord.objects.filter(car=carobj, owned_from__lte=owned_to, owned_to__gte=owned_from)
            if owned_from and owned_to and owned_from >= owned_to:
                messages.warning(request, "Owned from date must be less than owned to date.")
                return render(request, 'addowner.html', {'form': carform, 'car': carobj})
            if overlapping_owners.exists():
                messages.warning(request, "This car is already owned by someone else during this period.")
                return render(request, 'addowner.html', {'form': carform, 'car': carobj})
            owner_record = carform.save(commit=False)
            owner_record.car = carobj
            owner_record.save()
            # Increment the no_previous_owners field of the car
            carobj.no_previous_owners += 1
            carobj.save()
            messages.success(request, 'Ownership record added successfully!')
            return redirect(reverse('cardetails', kwargs={'id': carobj.id}))
    
def destroyowner(request,id):
    """Delete an ownership """

    ownobj = OwnerRecord.objects.get(id=id)
    carid = ownobj.car.id
    ownobj.delete()
    messages.warning(request, 'Ownership record deleted successfully!')
    return redirect(reverse('cardetails', kwargs={'id': carid}))
