from django.shortcuts import render
import json
import requests
from requests_oauthlib import OAuth1
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from dotenv import load_dotenv
import os

#This builds the database for products to access in each individual template
#This will provide the complimentary program to the cart
load_dotenv()

# Create your views here.
def home(request):
    img=[
        'https://media.istockphoto.com/photos/punching-bag-boxer-picture-id638813420?b=1&k=20&m=638813420&s=170667a&w=0&h=TGPUwYxSAiZ6HVo_FdObjdVmRYqbJ9Bqxzya4nx_jYI=',
        'https://media.istockphoto.com/photos/blood-sport-picture-id535030483?b=1&k=20&m=535030483&s=170667a&w=0&h=MR-pinRGN-nlq8ZHH5UiEicPKQTlGpgrZ987MiwWlCs=',
        'https://media.istockphoto.com/photos/athletic-woman-weightlifting-in-the-gym-picture-id1265043284?b=1&k=20&m=1265043284&s=170667a&w=0&h=iTKFg8Y_JINeIQIggxqdbCiSWuZLvLMUjVGKGhyKpc8='
        ]
    context={
        'img':img
    }
    return render(request, 'ecom_app/home.html', context)

@csrf_exempt
def fitness(request):
    if request.method=='GET':
        fitness_products=Fitness.objects.all()
        context={
            'product':fitness_products
            }
        return render(request, 'ecom_app/fitness.html', context)
    #this works with the front end to receive the items ID so we could pull the item and create a cart item
    #the same process will be repeated in the the following views
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            item=Fitness.objects.get(id=body['item'])
            new_item=Cart.objects.create(img_url= item.img_url, title=item.title, price=item.price)
            return JsonResponse({'item':'added to cart'})
        except Exception as e:
            return JsonResponse({'success':False})

@csrf_exempt
def barbells(request):
    if request.method=='GET':
        barbell_products=Barbells.objects.all()
        context={
            'product':barbell_products,
        }
        return render(request, 'ecom_app/barbells.html', context)
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            item=Barbells.objects.get(id=body['item'])
            new_item=Cart.objects.create(img_url= item.img_url, title=item.title, price=item.price)
            return JsonResponse({'item':'added to cart'})
        except Exception as e:
            return JsonResponse({'success':False})
        
        
@csrf_exempt
def dumbbells(request):
    if request.method=='GET':
        dumbbell_products=Dumbbells.objects.all()
        context={
            'product':dumbbell_products
        }
        return render(request, 'ecom_app/dumbbells.html', context)
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            item=Dumbbells.objects.get(id=body['item'])
            new_item=Cart.objects.create(img_url= item.img_url, title=item.title, price=item.price)
            return JsonResponse({'item':'added to cart'})
        except Exception as e:
            return JsonResponse({'success':False})
        
        

@csrf_exempt
def cart(request):
    if request.method=='GET':
        supply=Cart.objects.all()
        total=Cart.objects.aggregate(Sum('price'))
        total=total['price__sum']
        context={
            'total':total,
            'supply':supply
        }
        return render(request, 'ecom_app/cart.html', context)
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            item=Cart.objects.get(id=body['item'])
            item.delete()
            return JsonResponse({'success':True})
        except Exception as e:
            return JsonResponse({'success':False})
        
        

def product(request):
    item=request.POST.get("item")
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
    endpoint = f"http://api.thenounproject.com/icon/{item}"
    API_response = requests.get(endpoint, auth=auth)
    JSON_response=API_response.json()
    img_url=JSON_response['icon']['preview_url']
    img={
        'img':img_url
    }
    return render(request, 'ecom_app/search.html', img)