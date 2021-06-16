from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class Bug:  
    def __init__(self, name, scientific, description, location, ):
        self.name = name
        self.scientific = scientific
        self.description = description
        self.location = location

bugs = [
    Bug('American Bumble Bee', 'Bombus pensylvanicus', 'Black and yellow, stinger', 'Southern North America, through America, to Mexico'),
    Bug('Tarantula Hawk', 'Pepsis formosa', 'Blue-black exoskeleton, orange wings, powerful sting', 'India to Southeast Asia, Africa, Europe, Australia, and the Americas'),
    Bug('Jewel Wasp', 'Ampulex compressa', 'Emerald in color, half an inch in size', 'Africa, Asia, a few Pacific Islands'),
    Bug('Tropical Fire Ant', 'Solenopsis geminata', 'Deep red, pinchers at front of head half size of body', 'Texas to Florida, and South Carolina')
]




def home(request):
    return HttpResponse('<h1>Hello Bug Freak</h1>')

def about(request):
    return render(request, 'about.html')

def bugs_index(request):
    return render(request, 'bugs/index.html', {'bugs' : bugs})
