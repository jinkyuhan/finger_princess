from .models import *
from rest_framework import serializers


class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = ('id', 'name', 'point')


class GpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpu
        fields = ('id', 'name', 'point')


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ('id', 'name', 'weight', 'cpu', 'gpu', 'ram',
                  'ssd', 'hdd', 'resolution', 'display', 'price')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'rec_cpu_itl', 'rec_cpu_amd', 'rec_gpu_itl',
                  'rec_gpu_amd', 'rec_gpuram', 'rec_ram', 'rec_storage')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'name', 'rec_cpu', 'rec_gpu', 'rec_ram')


class LaptopPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopPerformance
        fields = ('id', 'name', 'weight', 'cpu', 'cpu_point', 'gpu', 'gpu_point', 'ram',
                  'ssd', 'hdd', 'resolution', 'display', 'price')


class GameRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRequirements
        fields = ('id', 'name', 'rec_cpu', 'rec_cpu_point', 'rec_gpu',
                  'rec_gpu_point', 'rec_gpuram', 'rec_ram', 'rec_storage')


class ProgramRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramRequirements
        fields = ('id', 'name', 'rec_cpu', 'rec_cpu_point',
                  'rec_gpu', 'rec_gpu_point', 'rec_ram')
