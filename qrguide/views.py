from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader 
from django.urls import reverse 

def index_view(request): 
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))

def about_view(request): 
    template = loader.get_template("about.html")
    return HttpResponse(template.render({}, request))

def college_view(request): 
    template = loader.get_template('college.html') 
    return HttpResponse(template.render({}, request))

def block_view(request, block_id): 
    template = loader.get_template('block.html')
    image = f"b{block_id}"
    image_url = 'images/{}.jpg'.format(image) # for adding image file as a jinja variable to load static 
    context = {
        "image": image_url, 
    }
    return HttpResponse(template.render(context, request))

def floor_view(request, block_id, floor_id, marked):

    # marked values are true for images with marker representing the location of the QR Code  
    if marked: 
        image = f"ab{block_id}_{floor_id}" 
    else: 
        image = f"b{block_id}_{floor_id}"
    base_url = reverse("college")

    template = loader.get_template('floor.html')
    image_url = 'images/{}.jpg'.format(image)

    # Boolean values reprenseting whether we there is a floor above  
    # below the current floor 
    up = is_above(block_id=block_id, floor_id=floor_id)
    down = is_below(floor_id=floor_id)

    # URLS for floors above and below the current floor 
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

# Get the top floor_id of the current block             
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