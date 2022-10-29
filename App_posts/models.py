from django.conf import settings
from django.db import models
from App.models import User

class Post(models.Model):
    title       = models.CharField(max_length=200, blank=False)
    content     = models.TextField(blank=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    created_by  = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    image       = models.ImageField(upload_to="uploads/image", null=True, blank=True)
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        return "https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        