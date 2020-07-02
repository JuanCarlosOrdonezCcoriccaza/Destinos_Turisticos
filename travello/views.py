from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Bali'
    dest1.desc = "The bike of Bali."
    dest1.img = 'destination_1.jpg'
    dest1.price = 699.9
    dest1.offer = True;

    dest2 = Destination()
    dest2.name = 'Playas de Acapulco'
    dest2.desc = "Hotel Turistico 5 estrellas."
    dest2.img = 'destination_6.jpg'
    dest2.price = 599.9
    dest2.offer = False;

    dest3 = Destination()
    dest3.name = 'Bahía_NoSurf'
    dest3.desc = "Playas tranquilas de bajo oleaje."
    dest3.img = 'destination_8.jpg'
    dest3.price = 569.9
    dest3.offer = False;
    
    dests = [dest1,dest2,dest3]
    
    return render( request ,'index.html',{'dests':dests})

def login(request):
    return HttpResponse('login.html')