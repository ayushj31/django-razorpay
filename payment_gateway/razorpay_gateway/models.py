# Core Django imports
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class PaymentDetails(models.Model):
    razorpay_id = models.CharField(max_length=255)
    payment = JSONField(null=True, blank=True)