from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from django.http import JsonResponse
from .models import Property
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def home(request, *args, **kwargs):
    if (request.method == "GET"):
        #Serialize the data into json
        data = serializers.serialize("json", Property.objects.all())
        loaded_data = json.loads(data)
        pk = 1
        api_data = {'data': {}}
        for i in range(0, len(loaded_data)):
            api_data['data'][pk] = (loaded_data[i]['fields'])
            pk += 1
        
        # Turn the JSON data into a dict and send as JSON response
        return JsonResponse(api_data, safe=False)
    
    if (request.method == "POST"):
        # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        #create the new item
        newrecord = Property.objects.create(name=body['name'], address=body['address'], city=body['city'], state=body['state'])
        # Turn the object to json to dict, put in array to avoid non-iterable error
        data = json.loads(serializers.serialize('json', [newrecord]))
        # send json response with new object
        return JsonResponse(data, safe=False)


@csrf_exempt
def fetch_property_details(request):
    if (request.method == "GET"):
        city_name = json.loads(request.body.decode("utf-8"))
        # print(city_name['name'])
        data = serializers.serialize("json", Property.objects.filter(name=city_name['name']))
        loaded_data = json.loads(data)
        pk = 1
        api_data = {'data': {}}
        for i in range(0, len(loaded_data)):
            api_data['data'][pk] = (loaded_data[i]['fields'])
            pk += 1
        return JsonResponse(api_data, safe=False)
    
    # if (request.method == "POST"):
    #     body = json.loads(request.body.decode("utf-8"))
    #     newrecord = Property.objects.create(name=body['name'], address=body['address'], city=body['city'], state=body['state'])
    #     data = json.loads(serializers.serialize('json', [newrecord]))
    #     return JsonResponse(data, safe=False)


@csrf_exempt
def update_property_details(request):
    if (request.method == "GET"):
        body = json.loads(request.body.decode("utf-8"))
        # print(body)
        data = serializers.serialize("json", Property.objects.all())
        data = json.loads(data)
        # print(data)
        for i in range(len(data)):
            if (str(data[i]['pk']) == str(body['id'])):
                data[i]['fields']['name'] = body['name']
                data[i]['fields']['address'] = body['address']
                data[i]['fields']['city'] = body['city']
                data[i]['fields']['state'] = body['state']
                break
        loaded_data = data
        pk = 1
        api_data = {'data': {}}
        for i in range(0, len(loaded_data)):
            api_data['data'][pk] = (loaded_data[i]['fields'])
            pk += 1
        return JsonResponse(api_data, safe=False)


@csrf_exempt
def find_cities_by_state(request):
    if (request.method == "GET"):
        body = json.loads(request.body.decode("utf-8"))
        # print(body)
        data = serializers.serialize("json", Property.objects.filter(state=body['state']))
        data = json.loads(data)
        # print(data)
        loaded_data = data
        pk = 1
        api_data = {'data': {}}
        for i in range(0, len(loaded_data)):
            api_data['data'][pk] = (loaded_data[i]['fields'])
            pk += 1
        return JsonResponse(api_data, safe=False)


@csrf_exempt
def find_similar_properties(request):
    if (request.method == "GET"):
        body = json.loads(request.body.decode("utf-8"))
        # print(body)
        data = serializers.serialize("json", Property.objects.filter(id=body['id']))
        data = json.loads(data)
        print(data)
        data_to_show = serializers.serialize("json", Property.objects.filter(city=data[0]['fields']['city']))
        loaded_data = json.loads(data_to_show)
        pk = 1
        api_data = {'data': {}}
        for i in range(0, len(loaded_data)):
            api_data['data'][pk] = (loaded_data[i]['fields'])
            pk += 1
        return JsonResponse(api_data, safe=False)