
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from . import models

def baoxiu(request):
    if request.method == "POST":
        user_id = request.POST.get("userid")
        room = request.POST.get("conference")
        service = request.POST.get("service")
        equip = request.POST.get("content")
        if user_id is not None and room is not None and service is not None and equip is not None:
            try:
                equipment=models.equipment()
                equipment.user_id=user_id
                equipment.room=room
                equipment.service=service
                equipment.equip=equip
                equipment.save()
                print(1)
                return JsonResponse({
                    "status": 0,
                    "message": "Register Success"
                })
            except:
                return JsonResponse({
                    "status": 2,
                    "message": "提交失败"
                })

            
@require_http_methods(["GET"])
def show_baoxiu(request):
    response = {}
    user_id = request.GET.get('user_id','')
    try:
        if user_id == '':

            users = models.equipment.objects.filter()
        else:
            users = models.equipment.objects.filter(fome_id = user_id)
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def edit_baoxiu(request):
    response = {}
    response['error_num'] = 0

    user_id = request.GET.get('user_id','')
    try:
        users = models.equipment.objects.get(fome_id = user_id)
        users.state="已完成"
        users.save()
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)