from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=100,unique=True)
    unit_price = models.IntegerField()
    category = models.ManyToManyField('Category')
    image = models.ImageField(upload_to='images/category', null=True)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    name = models.CharField("Name", max_length=50)
    parent_category = models.ForeignKey('self',on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
