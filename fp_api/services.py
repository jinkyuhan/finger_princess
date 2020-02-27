from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from .serializers import *
import json


@csrf_exempt
def recommend(request):
    if request.method =="POST":
        print(request.body)
        body=json.loads(request.body.decode('utf-8'))
        print(body)
        print('GAME: ',body['games'])
        print('OUTDOOR: ',body['outdoor'])
        print('BAG: ',body['bag'])
        print('PROGRAMS: ',body['programs'])
        print('BUDGET: ',body['budget'])
        print('PRIORITY: ',body['priority'])
        queryset=Laptop.objects.filter(ram__gte=16)
        #queryset=Program.objects.get(name__startswith='unreal').rec_cpu_set.all()
        serializer=LaptopSerializer(queryset,many=True)
        return JsonResponse(serializer.data,safe=False)
    else:
        print('LOG:GET')
