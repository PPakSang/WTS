from django.db import models

# Create your models here.


class Test(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    check=models.IntegerField(default=1)



    def __str__(self) -> str:
        return self.name