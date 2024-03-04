from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name="homepage"),
    path('addbrand/', v.create_brand, name='addbrand'),
    path('brands/', v.view_brands, name='viewbrands'),
    path('addcolour/', v.create_colour, name='addcolour'),
    path('colours/', v.view_colours, name='viewcolours'),
    path('addcar/', v.create_car, name='addcar'),
    path('editcar/<int:id>/', v.edit_car, name='editcar'),
    path('delcar/<int:id>/', v.destroycar, name='delcar'),
    path('cardetails/<int:id>/', v.car_details, name='cardetails'),
    path('addowner/<int:id>/', v.add_owner, name='addowner'),
    path('delown/<int:id>/', v.destroyowner, name='delown'),
]
