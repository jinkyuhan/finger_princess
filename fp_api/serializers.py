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
        fields = ('id', 'name', 'min_cpu', 'min_gpu', 'min_gpuram', 'min_ram')
