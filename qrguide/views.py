from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader 

def college_view(request): 
    template = loader.get_template('college.html') 
    return HttpResponse(template.render({}, request))

def block_view(request, block_id): 
    template = loader.get_template('block.html')
    image = f"b{block_id}.jpg"
    context = {
        "image": image, 
    }
    return HttpResponse(template.render(context, request))