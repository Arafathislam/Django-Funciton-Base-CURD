
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show,name="addshow"),
    path('delete/<int:id>/',views.delete,name="deletedata"),
    path('update/<int:id>/',views.update,name="updatedata"),
]
