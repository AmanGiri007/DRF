from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.


def api_home(request, *args, **kwargs):
    print(request.GET)
    print(request.POST)
    body = request.body
    print(body)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data.keys())
    # data['headers'] = request.headers
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
