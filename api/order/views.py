from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import get_user_model
# Create your views here.


def valid_user_authentication(id, token):
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token :
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request, id, token):
    if valid_user_authentication(id, token):
        if request.method == 'POST':
            user_id=id
            transaction_id = request.POST['transaction_id']
            amount = request.POST['amount']
            products = request.POST['products']
            product_count = len(products.split(',')[:-1])
            
            # print("order view output :", user_id, transaction_id, amount, product_count)
            
            
            UserModel = get_user_model()
            
            try:
                user = UserModel.objects.get(pk=user_id)
                # print("user : ", user)
            except:
                return JsonResponse({'error':'User Does Not exists'})
            
            # 
            order = Order(user=user, transaction_id=transaction_id, total_amount=amount, total_products=product_count, products=products)
            order.save()
            return JsonResponse({'success': True, 'error': False})
        else:
            return JsonResponse({'error':'Not a POST method'})
    else:
        return JsonResponse({'error':'please re-login','code':'534'})

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer