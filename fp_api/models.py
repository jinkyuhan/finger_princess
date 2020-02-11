from django.db import models
# Create your models here.

class Cpu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    point=models.FloatField()
    class Meta:
        ordering=['point']


class Gpu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    point=models.FloatField()
    class Meta:
        ordering=['point']

class Laptop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    weight=models.IntegerField()
    gpu=models.ForeignKey(Gpu,on_delete=models.CASCADE,null=True)
    cpu=models.ForeignKey(Cpu,on_delete=models.CASCADE)
    ram=models.IntegerField()
    category_tag=models.CharField(max_length=30)
    hdd=models.IntegerField(null=True)
    ssd=models.IntegerField()
    resolution_choices=[
        ('SD','640x480'),
        ('HD','1280x720'),
        ('FHD','1920x1080'),
        ('4K UHD','3840x2160'),
        ('8K UHD','7680x4320')    
    ]
    resolution=models.CharField(max_length=6,choices=resolution_choices)
    display_choices=[
        (13,'(32~34)cm'),
        (14,'(35~36)cm'),
        (15,'(37~39)cm'),
        (16,'(40~42)cm'),
        (17,'(43~44)cm'),
    ]
    display=models.IntegerField(choices=display_choices)
    price=models.IntegerField()


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    min_cpu=models.ForeignKey(Cpu,on_delete=models.CASCADE)
    min_gpu=models.ForeignKey(Gpu,on_delete=models.CASCADE)
    min_gpuram=models.IntegerField(null=True)
    min_ram=models.IntegerField()