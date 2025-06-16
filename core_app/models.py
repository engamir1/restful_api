from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __str__(self):
        return self.name
