from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name="homepage"),
    path('addbrand/', v.create_brand, name='addbrand'),
    path('brands/', v.view_brands, name='viewbrands'),
]
