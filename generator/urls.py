"""generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from email.mime import base
from django.contrib import admin
from django.urls import path, include
from . import views 
from .views import employeeCreate
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'generator'

# router = routers.DefaultRouter()
# router.register('employees', views.EmployeeList, basename='employees')
# router.register('employeenew', views.EmployeeDetail, basename='employeenew')

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('generator/', include('rest_framework.urls', namespace='rest_framework'))
# ]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('employee', EmployeeList, name='employeelist'),
#     path('employee/new', staffnew, name='employeenew'),
#     # path('', include(('generator.urls', 'generator'), namespace='generator'))   
# ]

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('employee-list/', views.employeelist,name="employee-list"),
    path('employee-create/', employeeCreate, name="employee-create"),
    path('employee-update/<str:pk>', views.employeeUpdate, name="employee-update"),
    path('employee-delete/<str:pk>', views.employeeDelete, name="employee-delete")
]
urlpatterns = format_suffix_patterns(urlpatterns)