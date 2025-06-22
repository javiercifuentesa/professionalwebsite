from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    # content = models.TextField()
    content = RichTextField(verbose_name="Content", config_name='extends')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Service"
        verbose_name_plural = "Services"