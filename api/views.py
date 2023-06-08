from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(response):
    return JsonResponse([
        {
            'further routes': {
                'for categories' : 'category/',
                'for products' : 'product/',
                'for user' : 'user/',
                'for order' : 'order/',
                'for payment options' : 'payment/'
            }
        }
    ], safe=False) # In order to allow non-dict objects to be serialized set the "safe" parameter to "False".