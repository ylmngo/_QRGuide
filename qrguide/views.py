from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader 
from django.urls import reverse 

def college_view(request): 
    template = loader.get_template('college.html') 
    return HttpResponse(template.render({}, request))

def block_view(request, block_id): 
    template = loader.get_template('block.html')
    image = f"b{block_id}"
    image_url = 'images/{}.jpg'.format(image) 
    context = {
        "image": image_url, 
    }
    return HttpResponse(template.render(context, request))

def floor_view(request, block_id, floor_id, marked):
    if marked: 
        image = f"ab{block_id}_{floor_id}" 
    else: 
        image = f"b{block_id}_{floor_id}"
    base_url = reverse("college")

    template = loader.get_template('floor.html')
    image_url = 'images/{}.jpg'.format(image)
    up = is_above(block_id=block_id, floor_id=floor_id)
    down = is_below(floor_id=floor_id)
    floor_up = base_url + 'block/{}/floor/{}/marker/{}'.format(block_id, floor_id + 1, 0)
    floor_below = base_url + 'block/{}/floor/{}/marker/{}'.format(block_id, floor_id - 1, 0)

    context = {
        'image' : image_url, 
        'up' : up, 
        'down' : down, 
        'floor_up' : floor_up, 
        'floor_below' : floor_below  
    }

    return HttpResponse(template.render(context, request))
        
def get_max_floor(block_id): 
    match block_id: 
        case 1: 
            max_floors = 4 
        case 2: 
            max_floors = 2 
        case 3: 
            max_floors = 0 
        case 4: 
            max_floors = 3 
        case 5: 
            max_floors = 6 
    
    return max_floors

def is_above(block_id, floor_id): 
    max_floor = get_max_floor(block_id)
    up = False 
    if floor_id < max_floor: 
        up = True 
    return up

def is_below(floor_id): 
    down = False 
    if floor_id > 0: 
        down = True 
    return down 