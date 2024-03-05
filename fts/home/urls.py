from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as v

urlpatterns = [
    # Home page
    path('', v.home, name="homepage"),
    # Brand URLs
    path('addbrand/', v.create_brand, name='addbrand'),
    path('brands/', v.view_brands, name='viewbrands'),
    # Colour URLs
    path('addcolour/', v.create_colour, name='addcolour'),
    path('colours/', v.view_colours, name='viewcolours'),
    # Car/Owner URLs
    path('addcar/', v.create_car, name='addcar'),
    path('editcar/<int:id>/', v.edit_car, name='editcar'),
    path('delcar/<int:id>/', v.destroycar, name='delcar'),
    path('cardetails/<int:id>/', v.car_details, name='cardetails'),
    path('addowner/<int:id>/', v.add_owner, name='addowner'),
    path('delown/<int:id>/', v.destroyowner, name='delown'),
    # Authentication URLs
    path('register/', v.registration, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # User URLs
    path('users/', v.view_users, name='viewusers'),
    path('approve_user/<int:id>/', v.approve_user, name='approve_user'),
    path('delete_user/<int:id>/', v.delete_user, name='delete_user'),
]
