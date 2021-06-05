from django.db import models


class HelloCount(models.Model):
    hello_count = models.IntegerField()

    def __str__(self):
        return "Count : " + self.hello_count.__str__()
