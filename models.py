from django.db import models

# Create your models here.
class Payments(models.Model):
    name=models.CharField(max_length=100)
    amount=models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
