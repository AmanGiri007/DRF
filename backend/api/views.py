from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
# Create your views here.


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed"}, status=405)
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # print(request.headers)
    '''#For GET
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data['title'] = instance.title
        # data['content'] = instance.content
        # data['price'] = instance.price
        # data = model_to_dict(instance, fields=[
        #                      'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    '''
    # for post
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = serializer.data
        return Response(data)
    return Response({"invalid": "not good data"}, status=400)
