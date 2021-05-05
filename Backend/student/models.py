from django.db import models

# Create your models here.


class Test(models.Model):
    name=models.CharField(max_length=10)
    user_id = models.IntegerField(blank=True,null=True)
    status=(('o','참'),('x','불'))
    enroll = models.CharField(choices=status,max_length=1,null=True)

    def __str__(self) -> str:
        return self.name

class Test2(models.Model):
    date = models.DateField()