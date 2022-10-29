from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email           = models.EmailField(max_length=150, unique=True)
    image           = models.ImageField(upload_to='uplaods/images', blank=True, null=True)
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','username']
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return "https://bulma.io/images/placeholders/1280x960.png"