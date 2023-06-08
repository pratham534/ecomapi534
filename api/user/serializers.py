from rest_framework import serializers
# 👇👇 decorators are used when we need to make changes to a file by accessing the file indirectly from another file, and not directly modifying the property of that file
from rest_framework.decorators import authentication_classes, permission_classes
# 👇👇 hashers are used to encode the password into non-readable format
from django.contrib.auth.hashers import make_password
from .models import CustomUser

# 👇👇 HyperlinkedModelSerializer does not include id field by default, rather a url field. incase of url of images, using ModelSerializer may result in incomplete url, which prevent images to be rendered
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # 👇👇 new instance of the user is created using the data received as validated_data
        # mainly used when registering the user
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            #👇👇 password is not saved as usual, it is saved using set_password() function
            instance.set_password(password)
            
        instance.save()
        return instance
    
    # 👇👇 the instance of the current user is updated using the data received as validated_data
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                # 👇👇 the key value pair are updated using setattr() function
                setattr(instance, attr, value)

        instance.save()
        return instance
    
    class Meta:
        model = CustomUser
        extra_kwargs = {'password':{'write_only':True}}
        fields = ('name', 'email', 'password', 'phone', 'gender', 'is_active', 'is_staff', 'is_superuser')