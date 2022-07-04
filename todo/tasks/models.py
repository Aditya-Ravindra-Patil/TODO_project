from datetime import date
from pyexpat import model
from random import choices
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODO(models.Model):
    c_status=[
        ('c','complete'),
        ('p','pending'),
    ]

    c_priority=[
        ('1','1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
        ('4','4️⃣'),
        ('5','5️⃣'),
        ('6','6️⃣'),
        ('7','7️⃣'),
        ('8','8️⃣'),
        ('9','9️⃣'),
        ('10','🔟',)

    ]

    title= models.CharField(max_length=50)
    status=models.CharField(max_length=2, choices=c_status)
    date=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=10, choices=c_priority)
    user=models.ForeignKey(User, on_delete= models.CASCADE)
