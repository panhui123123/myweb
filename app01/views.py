import json

from aip import AipNlp
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from app01.models import *


# Create your views here.


def index(request):
    return HttpResponse('I am your father')


def user_list(request):
    if request.method != 'GET':
        return JsonResponse({'result': 1, 'msg': 'the method you request is not correct'})
    name = request.GET.get('name', '')
    if name:
        QuerySet = UserInfo.objects.filter(name__contains=name).values()
        res = list(QuerySet)
        return JsonResponse({'result': 0, 'msg': 'success', 'data': res})
    QuerySet = UserInfo.objects.values()
    res = list(QuerySet)
    return JsonResponse({'result': 0, 'msg': 'success', 'data': res})


def user_add(request):
    if request.method != 'POST':
        return JsonResponse({'result': 1, 'msg': 'the method you request is not correct'})
    request_params = json.loads(request.body)
    name = request_params['name']
    phone = request_params['phone']
    if not name or not phone:
        return JsonResponse({'result': 1, 'msg': 'params error'})
    UserInfo.objects.create(name=name, phone=phone)
    return JsonResponse({'result': 0, 'msg': 'successfully add userinfo'})


def user_edit(request):
    if request.method != 'POST':
        return JsonResponse({'result': 1, 'msg': 'the method you request is not correct'})
    request_params = json.loads(request.body)
    user_id = request_params['id']
    name = request_params['name']
    phone = request_params['phone']
    try:
        user = UserInfo.objects.get(id=user_id)
    except UserInfo.DoesNotExist:
        return JsonResponse({'result': 1, 'msg': 'the id you search is not found'})
    UserInfo.objects.filter(id=user_id).update(name=name, phone=phone)
    return JsonResponse({'result': 0, 'msg': 'successfully update userinfo'})


def user_delete(request):
    if request.method != 'POST':
        return JsonResponse({'result': 1, 'msg': 'the method you request id not correct'})
    request_params = json.loads(request.body)
    user_id = request_params['id']
    try:
        user = UserInfo.objects.get(id=user_id)
    except UserInfo.DoesNotExist:
        return JsonResponse({'result': 1, 'msg': 'the id you delete is not found'})
    UserInfo.objects.filter(id=user_id).delete()
    return JsonResponse({'result': 0, 'msg': 'successfully delete'})


def text_check(request):
    if request.method != 'GET':
        return JsonResponse({'result': 1, 'msg': 'the method you request is not correct'})
    APP_ID = '41863571'
    API_KEY = 'wmiGYK4Sq9kcF9CN6nHXUBXg'
    SECRET_KEY = 'pLZjadXWP3Cjgk4nie3aOEFLRStXdypW'
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    text = request.GET.get('input_text', '')
    before_text, after_text = "", ""
    check_list = []
    if text == "":
        before_text, after_text = "哥哥, 你输入为空啦, 这是默认占位文案", "哥哥, 你输入为空啦, 这是默认占位文案"
    else:
        result = dict(client.ecnet(text))
        before_text = result['text']
        after_text = result['item']['correct_query']
        check_list = result['item']['vec_fragment']
    data = {'result': 0,
            'data': {'before_text': before_text, 'after_text': after_text, 'check_list': check_list},
            'msg': '成功'}
    return JsonResponse(data)


