from django.urls import path
from . import views
app_name='bank'
urlpatterns = [
    path('',views.home,name='home'),
    path('cust/',views.user_listview.as_view(),name='list'),
    path('details/<int:pk>',views.user_detailview.as_view(),name='details'),
]
