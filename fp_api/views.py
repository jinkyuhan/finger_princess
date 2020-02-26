from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

class GpuViewSet(viewsets.ModelViewSet):
    queryset = Gpu.objects.all()
    serializer_class = GpuSerializer

class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset=Program.objects.all()
    serializer_class=ProgramSerializer

class LaptopPerformanceViewSet(viewsets.ModelViewSet):
    queryset=LaptopPerformance.objects.all()
    serializer_class=LaptopPerformanceSerializer
