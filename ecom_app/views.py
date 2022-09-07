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
bodybuilding=Cart.objects.get_or_create(
    img_url='https://cdn.sanity.io/images/dm4o0ui7/production/ab8622774dfd8bc6b2107656cc1d648ff48279b3-1200x600.png?w=900&h=450&auto=format',
    title='Body Building',
    price=0
    )
# The following creates fitness programs
bodybuilding=Fitness.objects.get_or_create(
    img_url='https://cdn.sanity.io/images/dm4o0ui7/production/ab8622774dfd8bc6b2107656cc1d648ff48279b3-1200x600.png?w=900&h=450&auto=format',
    title='Body Building',
    price=250.50
    )

Calisthenics=Fitness.objects.get_or_create(
    img_url='https://www.greatestphysiques.com/wp-content/uploads/2016/11/Hannibal-for-king-Calisthenics-1.jpg',
    title='Calisthenics',
    price=122.5
)

Cardiovascular=Fitness.objects.get_or_create(
    img_url='https://www.outsideonline.com/wp-content/uploads/2020/10/13/russell-dinkins-track_h.jpg?width=1200',
    title='Cardiovascular',
    price=75.75
)

# The following creates barbells
olympic_bar=Barbells.objects.get_or_create(
    img_url='https://www.garage-gyms.com/wp-content/uploads/2013/12/olympic-barbell-bandr-rogue.jpg',
    title='Olympic Barbell',
    price=122.5
)

hex_bar=Barbells.objects.get_or_create(
    img_url='https://cdn.shopify.com/s/files/1/0471/3879/9774/products/O7HB_main_1035x@2x.jpg?v=1636408675%202x',
    title='Hex Bar',
    price=130.75
)

multigrip_bar=Barbells.objects.get_or_create(
    img_url='https://garagegymlab.com/wp-content/uploads/2021/02/SFB010-1.jpg',
    title='Multigrip Bar',
    price=177.5
)

# The following creates fitness programs
individual_dumbbell=Dumbbells.objects.get_or_create(
    img_url='https://www.technogym.com/wpress/wp-content/uploads/2019/04/Technogym-hexagonal-dumbbells_fb-1.jpg',
    title='Individual Dumbbells',
    price=77.5
)

adjustuble_dumbbells=Dumbbells.objects.get_or_create(
    img_url='http://mobileimages.lowes.com/productimages/0c24b23c-b9eb-4a62-a325-8faba2974e20/46594320.jpg',
    title='Adjustuble Dumbbells Pro',
    price=277.5
)

adjustuble_dumbbells_ecom=Dumbbells.objects.get_or_create(
    img_url='https://cdn.shopify.com/s/files/1/0575/5401/0306/t/15/assets/acf.Adjustable-Dumbbell-Pair-Main.png?v=1635535324',
    title='Adjustuble Dumbbells',
    price=153.89
)

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