from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree
# 👉👉 https://developer.paypal.com/braintree/docs/start/hello-server/python
# Create your views here.

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='hxpc3gpqtq6yffv8',
    public_key='gnsdw4nz8xhv4544',
    private_key='26b2110ab7a3c275889234114230375a'
  )
)

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
def generate_token(request, id, token):
    if not valid_user_authentication(id, token):
        return JsonResponse({
            'error':'Invalid Session. Login again'
        })
        
    return JsonResponse({
        'clientToken':gateway.client_token.generate(),
        'success':True
    })
    
    
@csrf_exempt
def payment_process(request, id, token):
    if not valid_user_authentication(id, token):
        return JsonResponse({
            'error':'Invalid Session. Login again'
        })
        
    paymentMethodNonce = request.POST['paymentMethodNonce']
    amount = request.POST['amount']
    
    result = gateway.transaction.sale({
        "payment_method_nonce": paymentMethodNonce,
        "amount": amount,
        "options": {
            "submit_for_settlement": True
        }
    })
    
    if result.is_success:
        return JsonResponse({
            'success':result.is_success,
            'transaction':{
                'id':result.transaction.id,
                'amount':result.transaction.amount
            }
        })
    else:
        return JsonResponse({
            'error':True,
            'success':False
        })