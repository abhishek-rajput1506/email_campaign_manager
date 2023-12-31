from django.db import models
from django.utils import timezone
# Create your models here.
class Subscriber(models.Model): 
    email = models.EmailField(unique=True, null=False)
    first_name = models.TextField(null=False)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = 'subscribers'

class Campaign(models.Model):
    subject = models.TextField(null=False)
    preview_text = models.TextField()
    article_url = models.TextField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateField(null=False, default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.subject
    
    class Meta:
        db_table = 'campaigns'