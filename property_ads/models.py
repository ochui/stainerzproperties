from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from djmoney.models.fields import MoneyField
from django_mysql.models import JSONField, Model

User = get_user_model()


class Category(models.Model):

    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Ad(models.Model):
    # Agent
    agent = models.ForeignKey(User, on_delete=models.CASCADE)

    # Generic fields
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='NGN')
    is_negotiable = models.BooleanField(default=False)
    broker_fee = models.BooleanField(default=False)
    description = models.TextField()

    # extra field
    attrs = JSONField()

    # Ad location
    address = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ad"
        verbose_name_plural = "ads"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ad_detail", kwargs={"pk": self.pk})


class AdImage(models.Model):

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/ad/%Y')
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Update Image"
        verbose_name_plural = "Update Images"

    def __str__(self):
        return '{} ({})'.format(self.ad, self.position)

    def get_absolute_url(self):
        return reverse("UpdateImage_detail", kwargs={"pk": self.pk})
