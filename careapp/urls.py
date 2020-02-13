from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.fn_home),
    path('getwet/', views.fn_wet),
    path('getshine/', views.fn_shine),
    path('getbalance/', views.fn_balance),
    path('adlogin/', views.fn_admin),
    path('createplan/',views.fn_createplan),
    path('viewplan/',views.fn_viewplan),
    path('deleteservice/',views.fn_deleteService)
]
