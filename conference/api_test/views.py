from django.shortcuts import render

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from .models import Conference
import sys
sys.path.append("./")
from user.models import User
from form.models import Form

'''
会议室管理
'''
@require_http_methods(["POST"])
def add_conference(request):
    print(request,type(request))
    response = {}
    print(request.body)
    data = json.loads(request.body)
    print(type(data),data)
    try:
        conference = Conference(**data)
        print(conference)
        conference.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def update_conference(request):
    response = {}
    print(request.body)
    data = json.loads(request.body)
    print(type(data), data)
    try:
        Conference.objects.filter(id = data['id']).update(**data)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def select_conference(request):
    response = {}
    id = request.GET.get('id', '')
    try:
        conference = Conference.objects.get(id = id)
        response['conference'] = json.dumps(model_to_dict(conference))
        print(response['conference'])
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def select_conferenceByid(request):
    response = {}
    conference_id = request.GET.get('conference_id', '')
    try:
        conference = Conference.objects.filter(conference_id = conference_id)
        if not conference:
            response['isExist'] = 0
        else:
            response['isExist'] = 1
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_conferences(request):
    response = {}
    conference_id = request.GET.get('conference_id','')
    try:
        if conference_id == '':
            conferences = Conference.objects.filter()
        else:
            conferences = Conference.objects.filter(conference_id = conference_id)
        conferens = list(conferences.values())
        print(conferens)
        response['list'] = json.loads(serializers.serialize("json", conferences))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def delete_conference(request):
    response = {}
    print(response)
    id = request.GET.get('id', '')
    try:
        conference = Conference(id = id)
        conference.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
'''
用户管理
'''
@require_http_methods(["GET"])
def select_user(request):
    response = {}
    id = request.GET.get('id', '')
    try:
        user = User.objects.get(id = id)
        response['user'] = json.dumps(model_to_dict(user,exclude='image'))
        print(response['user'])
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def update_user(request):
    response = {}
    print(request.body)
    data = json.loads(request.body)
    print(type(data), data)
    try:
        User.objects.filter(id = data['id']).update(**data)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def editPassword(request):
    response = {}
    print(request.body)
    data = json.loads(request.body)
    print(type(data), data)
    try:
        User.objects.filter(user_id=data['user_id']).update(password = data['password1'])
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["POST"])
def add_user(request):
    response = {}
    print(request.body)
    data = json.loads(request.body)
    users = User.objects.filter(user_id = data['user_id'])
    # if len(users):
    #     print('ssss')
    #     response['msg'] = '用户名已经存在'
    #     response['error_num'] = 1
    #     return JsonResponse(response)
    try:
        user = User(**data)
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_users(request):
    response = {}
    user_id = request.GET.get('user_id','')
    try:
        if user_id == '':
            users = User.objects.filter()
        else:
            users = User.objects.filter(user_id = user_id)
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def delete_user(request):
    response = {}
    print(request)
    id = request.GET.get('id', '')
    try:
        user = User(id = id)
        user.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_forms(request):
    response = {}
    user_id = request.GET.get('user_id','')
    try:
        forms = Form.objects.filter(user_id = user_id)
        print(forms)
        response['list'] = json.loads(serializers.serialize("json", forms))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def delete_form(request):
    response = {}
    print(response)
    id = request.GET.get('id', '')
    try:
        form = Form(id = id)
        form.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_meeting(request):
    response = {}
    user_id = request.GET.get('user_id','')
    user_name = User.objects.get(user_id = user_id).name
    try:
        forms = Form.objects.filter()
        forms = list(forms.values())
        new_form = []
        for item in forms:
            temp = item['Participants'].split(',')
            item.pop('data')
            if user_name in temp:
                new_form.append(item)
        print(new_form)
        response['list'] = json.dumps(new_form, ensure_ascii=False)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['error_num'] = 1
    return JsonResponse(response)