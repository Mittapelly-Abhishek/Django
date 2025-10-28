from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import Employees
from django.views.decorators.http import require_http_methods
import json
from django.forms.models import model_to_dict
from . serializers import EmployeeSerializers


# # Create your views here.

def get_user(req,user_id=None):
    if req.method=="GET":
        if user_id:
            try:
                employee=Employees.objects.get(id=user_id)
                data={"id":employee.id,
                      "name":employee.name,
                      "phone":employee.phone,
                      "department":employee.department,
                      "salary":employee.salary,
                      "date_joined":employee.date_joined}
                return JsonResponse({"user_data":data},status=200)
            except Employees.DoesNotExist:
                return JsonResponse({"error":f"user with id {user_id} is not found"},status=404)
        
        else:
            employees=Employees.objects.all().values()
            return JsonResponse({"user_data":list(employees)},status=200)

@csrf_exempt   
@require_http_methods(["POST"])             
def add_user(req):
    try:
        data=json.loads(req.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error":"invalid json"},status=400)
    
    user_name=data.get("name")
    user_phone=data.get("phone")
    user_department=data.get("department")
    user_salary=data.get("salary")
    user_date_joined=data.get("date_joined")

    if not user_name or not user_salary:
        return JsonResponse({"error":"name and salary are required"},status=400)
    employee=Employees.objects.create(name=user_name,phone=user_phone,department=user_department,
        salary=user_salary,date_joined=user_date_joined)
    modify_data=model_to_dict(employee)

    return JsonResponse({"user updated":modify_data},status=201)

@csrf_exempt
@require_http_methods(["PATCH"])
def update_user(request,user_id):
    try:
        employee=Employees.objects.get(id=user_id)
    except Employees.DoesNotExist:
        return JsonResponse({"error":f"user with id {user_id} is not found"},status=404)
    
    try:
        data=json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error":"invalid json data"},status=400)
    
    if "name" in data:
        employee.name=data["name"]
    if "phone" in data:
        employee.phone=data["phone"]
    if "department" in data:
        employee.department=data["department"]
    if "salary" in data:
        employee.salary=data["salary"]
    if "date_joined" in data:
        employee.date_joined=data["date_joined"]
    
    employee.save()

    employee_updated=model_to_dict(employee)

    return JsonResponse({"user updated succesfully":employee_updated})


@csrf_exempt
@require_http_methods(["PUT"])
def update_user_put(req,user_id):
    try:
        employee=Employees.objects.get(id=user_id)
    except Employees.DoesNotExist:
        return JsonResponse({"erorr":f'user with id{user_id} is not found'},status=404)
    
    try:
        data=json.loads(req.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"erorr":"invalid json data"},status=404)
    
    name=data.get("name")
    phone=data.get("phone")
    department=data.get("department")
    salary=data.get("salary")
    date_joined=data.get("date_joined")

    if not name or not salary :
        return JsonResponse({"error":"name or salary is required"})
    
    employee.name=name
    employee.phone=phone
    employee.department=department
    employee.salary=salary
    employee.date_joined=date_joined
    employee.save()

    employee_upd=model_to_dict(employee)

    return JsonResponse({"user updated succefully":employee_upd},status=200)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user(req,user_id):
    try:
        employee=Employees.objects.get(id=user_id)
        employee.delete()
        return JsonResponse({"msg":f"employee with id {user_id} is deleted successfully"})
    except Employees.DoesNotExist:
        return JsonResponse({"error":f"user with id {user_id} is not found"})
    


    
    
    







