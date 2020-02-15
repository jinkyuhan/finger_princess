from django.db import models
# Create your models here.


class Cpu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    point = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['point']


class Gpu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    point = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['point']


class Laptop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    weight = models.FloatField(null=True)
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE, null=True)
    ram = models.IntegerField(null=True)
    ssd = models.FloatField(null=True)
    hdd = models.FloatField(null=True)
    resolution = models.CharField(max_length=15, null=True)
    display_choices = [
        (13, '13인치 (32~34)cm'),
        (14, '14인치 (35~36)cm'),
        (15, '15인치 (37~39)cm'),
        (16, '16인치 (40~42)cm'),
        (17, '17인치 (43~44)cm'),
    ]
    display = models.IntegerField(choices=display_choices, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    min_cpu_itl = models.ForeignKey(Cpu, on_delete=models.CASCADE,null=True,related_name='min_itl_cpu_set')
    min_cpu_amd = models.ForeignKey(Cpu, on_delete=models.CASCADE,null=True,related_name='min_amd_cpu_set')
    min_gpu_itl = models.ForeignKey(Gpu, on_delete=models.CASCADE,null=True,related_name='min_itl_gpu_set')
    min_gpu_amd = models.ForeignKey(Gpu, on_delete=models.CASCADE,null=True,related_name='min_amd_gpu_set')
    min_gpuram = models.IntegerField(null=True)
    min_ram = models.IntegerField()
    min_storage=models.IntegerField()

    def __str__(self):
        return self.name
