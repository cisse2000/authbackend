from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model  = User
        fields = ( 
            "__all__"
            # 'id',
            # 'username',
            # 'email',
            # 'password',
            # 'first_name',
            # 'last_name',
            # 'get_image',
        )