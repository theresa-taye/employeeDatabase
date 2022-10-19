# end point to access our data
from django.http import JsonResponse
from .models import employee
from .serializers import employeeSerializer , UpdateEmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .paginations import CustomPagination
from django.core.paginator import Paginator
# from rest_framework.pagination import PageNumberPagination
from generator import serializers
from django.http import HttpResponse
from django.shortcuts import render
import requests

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/employee-list',
        'Create':'/employee-create',
        'Update':'employee-update/<str:pk>/',
        'Delete':'employee-delete/<str:pk>/',
    }

@api_view(['GET', 'POST'])
def employeelist(request, format=None):
    # paginator = CustomPagination()

    if request.method =='GET':

        # get all the EMPLOYEES
        query = request.GET.get('q')
        if query:
           employees= employee.objects.filter(Q(employeeID__contains = query)|Q(mailAdd__contains = query))
        else:
            employees = employee.objects.all().order_by('-employedDT')
        paginator = Paginator(employees,2)
        page = request.GET.get('page',1)
        employees = paginator.page(page)
        # serialize them
        serializer = UpdateEmployeeSerializer(employees, many=True)
        # return json
        # staff= JsonResponse({'Employees':serializer.data})
        # return Response(serializer.data)
        return render(request, "employees.html", {'emp': serializer.data, 'staff':employees})

    elif request.method == 'POST':
        serializer = UpdateEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, "employees.html", {'emp': serializer.data})



@api_view(['GET','POST'])
def employeeUpdate(request,pk):
    context ={}
    emp = employee.objects.get(employeeID=pk)
    serializer = employeeSerializer(emp, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect("employee-list")
        # return Response({'serializer': serializer, 'data': emp})
            # add form dictionary to context
    context["e"] = emp
 
    return render(request, "update.html", context)
    return render(request, "generateID.html", {'emp': serializer.data})
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

# @api_view(['DELETE','GET'])


# delete view for details
def employeeDelete(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(employee, employeeID = pk)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect("employee-list")
 
    return render(request, "delete.html", context)

#create view to access each employee detail
# @api_view(['GET', 'PUT','DELETE'])
# def employeedetail(request,id, format=None):
#     try:
#         emp =  employee.objects.get(pk=id)
#     except employee.DoesNotExist:
#         return Response (status=status.HTTP_404_NOT_FOUND)
   
#     serializer=employeeSerializer
#     if request.method =='GET':
#         serializer = employeeSerializer(emp)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = employeeSerializer(emp, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         # return Response({'serializer': serializer, 'data': emp})
#         return render(request, "generateID.html", {'emp': serializer.data})
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#             emp.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
 
# update API data
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView


# view to create new employee
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404, redirect

# class EmployeeList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'employees.html'

#     def get(self, request):
#         queryset = employee.objects.all()
#         return Response({'emp': queryset})

from rest_framework import generics
# class EmployeeDetail(generics.CreateAPIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'generateID.html'

#     def get(request,format=None):
#         emp = employee.objects.filter()
#         serializer = UpdateEmployeeSerializer(emp, many=True)
#         return Response({'serializer': serializer, 'emp': emp})

#     def post(request,format=None):
#         emp = employee.objects.filter()
#         serializer = UpdateEmployeeSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'emp': emp})
#         serializer.save()
#         return redirect('employeelist')

# employee list with search feature
# from rest_framework.filters import SearchFilter, OrderingFilter

# class EmployeeListView(generics.ListAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employeeSerializer
#     filter_backends = (SearchFilter, OrderingFilter)
#     search_fields = ('employeeID', 'mailAdd')




    # template_name = 'generateID.html'
@api_view(['GET','POST'])

def employeeCreate(request,format=None):
    emp = employee(id,request.POST)
    if request.method == "POST":
        print(request.data)
        serializer=employeeSerializer(emp,data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return redirect('employee-list')
        # return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
    else:
        emp = employee
    serializer = employeeSerializer
    return render(request, 'generateID.html', {'serializer': serializer, 'emp': emp})
        # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def employeeCreate(request):
#     table_data= requests.get('http://127.0.0.1:1500/api/').json() 
#     if request.method == "POST":
#         url = 'https://xom2rj64bc.execute-api.us-east-1.amazonaws.com/dev/details'
#         payload = {'tasktype':'create','firstname':request.POST.get("firstname"),
#             'role':request.POST.get("role"),
#             'department':request.POST.get("department"),
#             'gender':request.POST.get("gender"),
#             'date':request.POST.get("date")}
#         r = requests.post(url, data = payload)
        # if r.status_code == 200:
        #     data = r.json()
        #     return Response(data, status=status.HTTP_200_OK)
        # return render(request, 'generateID.html', {'emp': r})
  
#  #connect to AWS API

# # Create your views here.
# @api_view(['GET','POST'])
# def employeelist(request):
#     #pull data from third party aws api
#     response = requests.get('https://xom2rj64bc.execute-api.us-east-1.amazonaws.com/dev/details')
#     #convert reponse data into json
#     staff = response.json()
#     print(staff)
#     return render(request, "employees.html", {'emp': staff})
    