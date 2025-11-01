from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import UserReg

# Create your views here.

def validate_file(file_obj):
    max_size=5*1024*1024

    if file_obj.size>max_size:
        return False,'File is too large.Max size is 5 MB.'
    
    allowed_type=['image/jpeg','image/png']

    if file_obj.content_type not in allowed_type:
        return False,"invalid file type.Allowed:jpeg,png."
    
    return True,'valid file'


@csrf_exempt
def reg_user(req):
    user_name=req.POST.get("name")
    user_email=req.POST.get("email")
    user_mobile=req.POST.get("mobile")
    file_obj=req.FILES['profile_pic']

    is_valid_file,msg=validate_file(file_obj)

    if is_valid_file:
        pass
    else:
        return HttpResponse(msg)
    
    new_user=UserReg.objects.create(name=user_name,email=user_email,mobile=user_mobile,image=file_obj)

    return HttpResponse("user added successfully")