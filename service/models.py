from django.db import models

# Create your models here.

class assignments_to_uploads(models.Model):
    a_img1=models.ImageField(upload_to='service/static/images')
    a_img2=models.ImageField(upload_to='service/static/images',default="")
    a_img3=models.ImageField(upload_to='service/static/images',default="")
    a_img4=models.ImageField(upload_to='service/static/images',default="")
    a_img5=models.ImageField(upload_to='service/static/images',default="")
    a_title=models.CharField(max_length=250)
    a_description=models.CharField(max_length=250)