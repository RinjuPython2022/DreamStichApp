from django.db import models

# Create your models here.
class Contacts(models.Model):
    cust_name=models.CharField(max_length=100)
    cust_phone=models.CharField(max_length=10)
    cust_email=models.EmailField(max_length=100)
    cust_remark=models.TextField()
    
    def __str__(self):
        return self.cust_name