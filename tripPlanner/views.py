from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.urls import reverse

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def places(request):
    context = {}
    query = request.GET.get('q')
    mymembers = Place.objects.all().values()
    dk = {'mymembers':mymembers,}
    if query:
        q = query.title()
        member = Place.objects.filter(name=q)
        for info in member:
            context["LocationId"]=info.locationId
            context["Name"]=info.name
            context["Description"]=info.desc
            context["Image"]=info.img
            context["ParentId"] = info.parentId
        dk.update(context)
        print(dk)
        return render(request,'main.html',dk)
    else:
        return redirect('index')

place= None

def add(request):
    context = {}
    template = loader.get_template('rating.html')
    locationid = 0
    global place
    if request.method=="POST":
        action = request.POST.get('addrecord')
        if action == 'review':
            id = int(request.POST['locationId'])
            locationid=id
            mymembers = Feedback.objects.filter(locationId=id)
            context = {'mymembers':mymembers}
            place = Place.objects.get(locationId=locationid)
            
        if action == 'rates':
            if place:
                rates = request.POST['rating']
                comment = request.POST['review']
                member = Feedback.objects.create(locationId=place,rating=rates, review = comment)
                return HttpResponseRedirect(reverse('add'))
                
    return HttpResponse(template.render(context,request))
