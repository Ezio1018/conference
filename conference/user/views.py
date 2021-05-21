
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from . import models
import face_recognition
import base64
from io import BytesIO
import re

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np


@require_http_methods(["POST"])
def login_user(request):
    islogin=False
    if request.method == "POST":
        data = json.loads(request.body)
        userid = data.get("username")
        password = data.get("password")
        if userid is not None and password is not None:
            try:
                user = models.User.objects.get(user_id=userid)
                if user.password == password:
                    return JsonResponse({
                        "status": 0,
                        "message": "Login Success",
                        "username": user.name,
                        "identity": user.identity
                    })
                else:
                    return JsonResponse({
                    "status": 1,
                    "message": "登录失败, 请检查密码是否输入正确."
                })
            except:
                return JsonResponse({
                    "status": 1,
                    "message": "登录失败, 请检查用户名是否输入正确."
                })
        else:
            return JsonResponse({
                "status": 2,
                "message": "参数错误"
            })


def register(request):
    if request.method == "POST":
        # data = json.loads(request.body.decode('utf-8'))
        if request.GET.get("select") is not None:
            print(2)
            select_username = request.POST.get("select_username")
            print(select_username)
            try:
                models.User.objects.get(user_id=select_username)
                return JsonResponse({
                    "status": 0,
                    "is_indb": 1
                })
            except:
                return JsonResponse({
                    'status': 0,
                    "is_indb": 0
                })
        username = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        userid=request.POST.get("userid")
        department=request.POST.get("department")
        gender=request.POST.get("gender")
        image=request.FILES.get('image')
        identity=request.POST.get("identity")
        print(username)
        print(password)
        print(email)
        print(userid)
        print(department)
        print(gender)
        print(image)
        print(identity)
        if userid is not None and password is not None and email is not None and department is not None and image is not None and username is not None and gender is not None:
            try:
                user=models.User()
                user.user_id=userid
                user.department=department
                user.password=password
                user.email=email
                user.gender=gender
                user.name=username
                user.image=image
                user.identity=identity
                user.save()
                print(1)
                return JsonResponse({
                    "status": 0,
                    "message": "Register Success"
                })
            except:
                return JsonResponse({
                    "status": 2,
                    "message": "注册失败, 该用户已经存在."
                })

    else:
        return JsonResponse({
            "status": 1,
            "message": "error method"
        })
def image_compare_image(img1,img2):

    im1 = face_recognition.load_image_file(img1)
    im2 = face_recognition.load_image_file(img2)
    
    try:
        img1_encoding = face_recognition.face_encodings(im1)[0]
        img2_encoding = face_recognition.face_encodings(im2)[0]
        known_faces = [img1_encoding]
        face_distances = face_recognition.face_distance([img1_encoding], img2_encoding)
        print(face_distances)
        return face_distances
    except Exception as e:
        print(e)
        

def read_file_from_base64(base64img):
    base64_data = re.sub('^data:image/.+;base64,', '', base64img)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    return image_data

@require_http_methods(["POST"])
def detect(request):
    if request.method == "POST":
        test_image=request.POST.get('test_image')[23:]
        id=request.POST.get("id")
        imagedata = base64.b64decode(test_image)
        file = open('1.jpeg',"wb")
        file.write(imagedata)
        file.close()
        # print(test_image)
        # test_image =read_file_from_base64(test_image)
        if id is not None and test_image is not None:
            user = models.User.objects.get(user_id=id)
            print(user.image)
            result=image_compare_image("1.jpeg",user.image)
            # print(result)
            if(result==None):
                return JsonResponse({
                    "status": 1,
                    "message": "face recognition not found",
                })
            elif(result<=0.4):
                return JsonResponse({
                    "status": 0,
                    "message": "face recognition Success",
                })
            else:
                return JsonResponse({
                    "status": 2,
                    "message": "face recognition Falied"
                })

            
