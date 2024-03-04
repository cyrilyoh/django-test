from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BrandForm
from .models import Brand

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

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Brand.objects.create(name=name)
            return redirect('brand_list')  # Redirect to a URL after successful submission
    else:
        form = BrandForm()
    
    return render(request, 'your_template.html', {'form': form})

def view_brands(request):
    """ List all brands """

    brands = Brand.objects.all()
    return render(request, "viewbrands.html", {'data':brands})