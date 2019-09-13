from django.db import models


class Organizer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Upfront(models.Model):
    recoupable = models.BooleanField()
    organizer = models.ForeignKey(Organizer, on_delete=models.PROTECT)
    projection = models.FloatField()

