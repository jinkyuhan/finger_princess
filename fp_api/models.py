from django.db import models
from django_db_views.db_view import DBView
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
    img=models.CharField(max_length=150)
    url=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    rec_cpu_itl = models.ForeignKey(
        Cpu, on_delete=models.CASCADE, null=True, related_name='rec_itl_cpu_set')
    rec_cpu_amd = models.ForeignKey(
        Cpu, on_delete=models.CASCADE, null=True, related_name='rec_amd_cpu_set')
    rec_gpu_itl = models.ForeignKey(
        Gpu, on_delete=models.CASCADE, null=True, related_name='rec_itl_gpu_set')
    rec_gpu_amd = models.ForeignKey(
        Gpu, on_delete=models.CASCADE, null=True, related_name='rec_amd_gpu_set')
    rec_gpuram = models.IntegerField(null=True)
    rec_ram = models.IntegerField()
    rec_storage = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Program(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    rec_cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE, null=True)
    rec_gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE, null=True)
    rec_ram = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class LaptopPerformance(DBView):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    weight = models.FloatField(null=True)
    cpu = models.ForeignKey(Cpu, on_delete=models, null=True)
    cpu_point = models.FloatField()
    gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE, null=True)
    gpu_point = models.FloatField()
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
    img=models.CharField(max_length=150)
    url=models.CharField(max_length=1000)
    view_definition = """
        SELECT
        Laptop.id as id,
        Laptop.name as name,
        Laptop.weight as weight,
        Cpu.id as cpu_id,
        Cpu.point as cpu_point,
        Gpu.id as gpu_id,
        Gpu.point as gpu_point,
        Laptop.ram as ram,
        Laptop.ssd as ssd,
        Laptop.hdd as hdd,
        Laptop.resolution as resolution,
        Laptop.display as display,
        Laptop.price as price,
        Laptop.img as img,
        Laptop.url as url    
        FROM fp_api_laptop as Laptop,fp_api_cpu as Cpu,fp_api_gpu as Gpu
        WHERE Laptop.cpu_id = Cpu.id
        AND Laptop.gpu_id = Gpu.id
        UNION
        SELECT
        Laptop.id as id,
        Laptop.name as name,
        Laptop.weight as weight,
        Cpu.id as cpu_id,
        Cpu.point as cpu_point,
        NULL as gpu_id,
        0 as gpu_point,
        Laptop.ram as ram,
        Laptop.ssd as ssd,
        Laptop.hdd as hdd,
        Laptop.resolution as resolution,
        Laptop.display as display,
        Laptop.price as price,
        Laptop.img as img,
        Laptop.url as url    
        FROM fp_api_laptop as Laptop,fp_api_cpu as Cpu,fp_api_gpu as Gpu
        WHERE Laptop.cpu_id = Cpu.id
        AND Laptop.gpu_id is NULL
    """

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "LaptopPerformance"
        ordering = ['id']


class GameRequirements(DBView):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    rec_cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE, null=True)
    rec_cpu_point = models.FloatField()
    rec_gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE, null=True)
    rec_gpu_point = models.FloatField()
    rec_gpuram = models.IntegerField(null=True)
    rec_ram = models.IntegerField()
    rec_storage = models.IntegerField()

    view_definition = """
        SELECT
        Game.id as id,
        Game.name as name,
        Cpu.id as rec_cpu_id,
        Cpu.point as rec_cpu_point,
        Gpu.id as rec_gpu_id,
        Gpu.point as rec_gpu_point,
        Game.rec_gpuram as rec_gpuram,
        Game.rec_ram as rec_ram,
        Game.rec_storage as rec_storage
        FROM fp_api_game as Game,fp_api_cpu as Cpu,fp_api_gpu as Gpu
        WHERE Game.rec_cpu_itl_id = Cpu.id
        AND Game.rec_gpu_itl_id = Gpu.id
        UNION
        SELECT
        Game.id as id,
        Game.name as name,
        Cpu.id as rec_cpu_id,
        Cpu.point as rec_cpu_point,
        NULL as rec_gpu_id,
        0 as rec_gpu_point,
        Game.rec_gpuram as rec_gpuram,
        Game.rec_ram as rec_ram,
        Game.rec_storage as rec_storage
        FROM fp_api_game as Game,fp_api_cpu as Cpu,fp_api_gpu as Gpu
        WHERE Game.rec_cpu_itl_id = Cpu.id
        AND Game.rec_gpu_itl_id is NULL
    """

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "GameRequirements"
        ordering = ['id']


class ProgramRequirements(DBView):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    rec_cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE, null=True)
    rec_cpu_point = models.FloatField()
    rec_gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE, null=True)
    rec_gpu_point = models.FloatField()
    rec_ram = models.IntegerField()
    view_definition = """
        SELECT
        Program.id as id,
        Program.name as name,
        Cpu.id as rec_cpu_id,
        Cpu.point as rec_cpu_point,
        Gpu.id as rec_gpu_id,
        Gpu.point as rec_gpu_point,
        Program.rec_ram as rec_ram
        FROM fp_api_program as Program,fp_api_cpu as Cpu,fp_api_gpu as Gpu
        WHERE Program.rec_cpu_id = Cpu.id
        AND Program.rec_gpu_id = Gpu.id
        UNION
        SELECT
        Program.id as id,
        Program.name as name,
        Cpu.id as rec_cpu_id,
        Cpu.point as rec_cpu_point,
        NULL as rec_gpu_id,
        0 as rec_gpu_point,
        Program.rec_ram as rec_ram
        FROM fp_api_program as Program,fp_api_cpu as Cpu,fp_api_gpu as Gpu
        WHERE Program.rec_cpu_id = Cpu.id
        AND Program.rec_gpu_id is NULL
    """

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "ProgramRequirements"
        ordering = ['id']
