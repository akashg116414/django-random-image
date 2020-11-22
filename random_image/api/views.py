from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .models import Images
import random
import requests

def start_again(request): 
  
    id_list = list(Images.objects.filter(flag=1).values_list("image_id",flat=True))

    Images.objects.filter(image_id__in=id_list).update(flag=0)
    img_obj = Images.objects.filter(flag=0).values().first()
    print(img_obj)
    return render(request, 'home.html',img_obj)

    

def display_images(request): 
  
    image_id = random.randint(0,1084)
    
    url = f'https://picsum.photos/id/{image_id}/400/500'
    
    img_obj = Images.objects.filter(image_id=image_id,flag=0).values().first()
    if img_obj:
        Images.objects.filter(image_id=image_id).update(flag=1)
    else:
        Images.objects.create(image_id=image_id, url=url,flag=1)
        img_obj = Images.objects.filter(image_id=image_id).values().first()
        
    print(img_obj)
    return render(request, 'home.html',img_obj)


