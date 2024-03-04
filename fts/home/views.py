from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BrandForm, ColourForm, CarForm
from .models import Brand, Colour, Car

def home(request):
    return render(request, 'home.html')

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
    return render(request, "viewbrands.html", {'data':brands})

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
    cars = Car.objects.all()
    return render(request, 'home.html', {'data': cars})
