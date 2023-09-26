from django.db import models
from accounts.models import CustomUser

class Products(models.Model):
    title = models.CharField(max_length=100,unique=True)
    unit_price = models.IntegerField()
    category = models.ManyToManyField('Category')
    image = models.ImageField(upload_to='images/category', null=True)
    brand = models.ForeignKey('Brand',on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey('self',on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class Like(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, name='liked_user')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, name='liked_product')


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT,name='user_comments')
    content = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.PROTECT, name="comment_products")
