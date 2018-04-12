from django.db import models

class food(models.Model):
    food_id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    taste = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.IntegerField()

class restaurent(models.Model):
    restaurent_id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=15)

class user(models.Model):
    email = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=500)

class cart(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    food_id = models.ForeignKey(food, on_delete=models.CASCADE)
    qty = models.IntegerField()
