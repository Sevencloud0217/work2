from django.db import models
class LoginUser(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=32)
    username=models.CharField(max_length=32,null=True,blank=True)
    phone_number=models.CharField(max_length=11,null=True,blank=True)
    photo=models.ImageField(upload_to="images",null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(null=True,blank=True,max_length=4)
    address=models.TextField(null=True,blank=True)
    user_type=models.IntegerField(default=1)
    class Meta:
        db_table='login'
