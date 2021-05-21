
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse, response
from datetime import date
from django.db.models import Q
import json

import sys
sys.path.append("./")
from  api_test.models import Conference
from  user.models import User
from form.models import Form
# Create your views here.

@require_http_methods(["GET"])
def show_conference(request):
    response = {}
    conference_id = request.GET.get('conference_id','')
    try:
        if conference_id == '':
            conferences = Conference.objects.filter()
        else:
            conferences = Conference.objects.filter(conference_id = conference_id)
        response['list'] = json.loads(serializers.serialize("json", conferences))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_form(request):
    response = {}
    conference_id = request.GET.get('conference_id','')
    try:
        if conference_id == '':
            forms = Form.objects.filter()
        else:
            forms = Form.objects.filter(room = conference_id)
        response['list'] = json.loads(serializers.serialize("json", forms))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
@require_http_methods(["GET"])
def yy_conference(request):
    response = {}
    user_id = request.GET.get('user_id', '')
    conference_id = request.GET.get('conference_id', '')
    time_id = request.GET.get('time_id','')
    day = request.GET.get('day','')
    Participants =request.GET.get('Participants','')

    print(Participants)
    try:
        form = Form(room = conference_id,user_id= user_id,time_id=time_id,day=day,Participants = Participants,statu ='已预约')
        form.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_name(request):
    response = {}
    username ={}
    user_id = request.GET.get('user_id', '')
    own_level = User.objects.filter(user_id =user_id).values('level')
    own_level = own_level[0]['level']
    usr = User.objects.filter(level__lte=own_level).values('name')
    print(usr)
    for t,i in enumerate(usr):
        if i['name'] !='':
            username[t]=i['name']
    lent=len(username)
    username['length']=lent
    return JsonResponse(username,json_dumps_params={'ensure_ascii':False},safe=False)

@require_http_methods(["GET"])
def show_name_new(request):
    user_id = request.GET.get('user_id', '')
    own_level = User.objects.filter(user_id =user_id).values('level')
    own_level = own_level[0]['name']
    username ={}
    usr = User.objects.filter(own_level = user_id).values('name')
    for t,i in enumerate(usr):
        if i['name'] !='':
            username[t]=i['name']
    lent=len(username)
    username['length']=lent
    return JsonResponse(username,json_dumps_params={'ensure_ascii':False},safe=False)


@require_http_methods(["GET"])
def cancel_book(request):
    response ={}
    id1 = request.GET.get('id', '')
    print("dsdsdsdsdf",id1)
    Form.objects.filter(id=id1).update(statu='已取消')
    try:
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def sgin_in(request):
    conference_id = request.GET.get('conference_id', '')
    time_id = request.GET.get('time_id','')
    day = request.GET.get('day','')
    Form.objects.filter(Q(room=conference_id)|Q(time_id=time_id)|Q(day=day)).update(statu='已签到')

@require_http_methods(["GET"])
def update_forms(request):
    response ={}
    date_now = date.today()
    Form.objects.filter(Q(day__lt=date_now) & Q(statu='已预约')).update(statu='已取消')
    return JsonResponse(response)
@require_http_methods(["GET"])
def delete_form(request):
    response ={}
    id1 = request.GET.get('id', '')
    
    try:
        Form.objects.filter(Q(id=id1)).delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def draw_forms(request):
    roomlist = []
    time_id_list=[]
    day_list=[]
    res=[]
    room = Form.objects.values('room')
    time_id = Form.objects.values('time_id')  
    day = Form.objects.values('day')

    for t,i in enumerate(room):
        if i['room'] !='':
            roomlist.append(i['room'])
    for t,i in enumerate(time_id):
        if i['time_id'] !='':
            time_id_list.append(i['time_id'])
    for t,i in enumerate(day):
        if i['day'] !='':
            day_list.append(i['day'])
    res.append(roomlist)
    res.append(time_id_list)
    res.append(day_list)
    return JsonResponse(res,json_dumps_params={'ensure_ascii':False},safe=False)

@require_http_methods(["GET"])
def judge_yy(request):
    judge=0
    conference_id = request.GET.get('id','')
    time = request.GET.get('time','')
    day = request.GET.get('day','')
    id1 = Form.objects.filter(room=conference_id,day=day,time_id=time)
    if id1.exists():
        judge=1
    return JsonResponse(judge,json_dumps_params={'ensure_ascii':False},safe=False)

def participant(request):
    response = {}
    person_id = request.GET.get('participant_id','')
    conference_id = request.GET.get('conference_id','')
    person = User.objects.filter(user_id =person_id).values('name')
    person = person[0]['name']
    Participants = Form.objects.values('Participants')
    partcon =[]
    id1 = Form.objects.values('id')
    id_list=[]
    for i in id1:
        id_list.append(i['id'])
    for index,p in  enumerate(Participants):
        if p['Participants'] !='':
            strp=p['Participants'].split(",")
            for i in strp:
                if i==person:
                    partcon.append(id_list[index])
                    break
    q_objects = Q(id = partcon[0]) 
    if(len(partcon)>1):
        for t in partcon[1:]: 
            q_objects = q_objects | Q(id = t)
    if conference_id != '':
        q_objects = q_objects & Q(room =conference_id)
    try:
        data = Form.objects.filter(q_objects)
        response['list'] = json.loads(serializers.serialize("json", data))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)