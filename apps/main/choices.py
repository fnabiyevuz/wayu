from django.db import models


class PaymentType(models.TextChoices):
    PAYME = "Payme"
    OSON = "Oson"
    CLICK = "Click"
