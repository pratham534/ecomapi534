# 👉 for various permissions and authorisations, Django Authentication System : https://docs.djangoproject.com/en/4.2/topics/auth/default/
import random
# 👇👇 re provides operations for pattern matching, the presence of a pattern in a variable
import re
# from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Create your views here.
def generate_session_token():
    x = [chr(i) for i in range(97,123)] + [str(i) for i in range(10)]
    # print(x)
    return ''.join(random.choice(x) for _ in range(10))

# 👇👇 when making request from a different origin/site(e.g. a react website using api from DRF(django rest framework)) rather than the actual handler(e.g. the django backend), the function-based view(to which request was made) needs to be exempted from the protection of csrf(cross site request forgery) governed by django middlewares, which prevents request from other sites to make changes to views.
# 👇👇 Normally when you make a request via a form you want the form being submitted to your view to originate from your website and not come from some other domain. To ensure that this happens, you can put a csrf_token in your form for your view to recognize. If you add @csrf_exempt to the top of your view, then you are basically telling the view that it doesn't need the token.
@csrf_exempt
def signin(request):
    
    if not request.method == "POST":
        return JsonResponse({'error':'Send a post request to proceed'})
    
    username = request.POST['email']
    password = request.POST['password']
    
    if not re.match("^([A-Z|a-z|0-9](\.|_){0,1})+[A-Z|a-z|0-9]\@([A-Z|a-z|0-9])+((\.){0,1}[A-Z|a-z|0-9]){2}\.[a-z]{2,3}$", username):
        return JsonResponse({'error':'Enter a valid email'})
    
    # if not re.match("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$", password):
    #     return JsonResponse({'error':'password not a valid password'})
    
    # 👇👇 get_user_model() returns the current model being used for user authentication, Custom model or default model
    UserModel = get_user_model()
    
    try:
        # 👇👇 If you use get(), you expect one (and only one) item that matches your criteria. Get throws an error if the item does not exist or if multiple items exist that match your criteria.
        user = UserModel.objects.get(email=username)
        
        if user.check_password(password):
            # 👇👇 If you use filter(), you typically do this whenever you expect more than just one object that matches your criteria. If no item was found matching your criteria, filter() returns am empty queryset without throwing an error.
            user_dict = UserModel.objects.filter(email=username).values().first()
            # print(user_dict)
            user_dict.pop('password')
            # print(user_dict)
            
            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':'previous session already exists', 'exists': 'true'})
            
            token = generate_session_token()
            user.session_token = token
            user.save()
            # 👇👇 django's default login() function saves the current session of the user specified, using django session framework
            login(request, user)
            
            return JsonResponse({'token':token, 'user': user_dict})
            
        else:
            return JsonResponse({'error':'wrong password', 'exists': 'true'})
        
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'User does not exist', 'exists': 'false'}) 
    
def signout(request, id):
    logout(request)
    
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'UserID invalid'})
    
    return JsonResponse({'success':'Logout Successful'})

    
class UserViewSet(viewsets.ModelViewSet):
    # 
    permission_classes_by_action = {'create':[AllowAny]}
    
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer
    
    # 
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]