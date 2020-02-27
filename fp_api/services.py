from django.db.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .serializers import *
import json

# max의 경우 피연산자항이 None일 경우 에러가 난다. -> 대체 function


def comparator(a, b):
    if a != None and b != None:
        return max(a, b)
    elif a != None and b == None:
        return a
    elif a == None and b != None:
        return b
    else:
        return 0


@csrf_exempt
def recommend(request):
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))

        # 사용자 입력을 정리해서 변수에 각각 할당해준다.
        games = [name for (name, value)
                 in body['games'].items() if value == True]
        outdoor = body['outdoor']
        bag = body['bag']
        programs = [name for (name, value)
                    in body['programs'].items() if value == True]
        budget = body['budget']
        priority = body['priority']

        # gamerequirement view(각 게임에 대한 cpu,gpu 요구량 및 ram , 등을 정리한 view)에서 사용자가 입력한 게임 리스트중에서 가장 높은 사양을 뽑는다.
        game_data = GameRequirements.objects.filter(name__in=games).aggregate(
            Max('rec_cpu_point'), Max('rec_gpu_point'), Max('rec_ram'), Max('rec_storage'))
        game_cpu_point, game_gpu_point, game_ram, game_storage = game_data['rec_cpu_point__max'], game_data[
            'rec_gpu_point__max'], game_data['rec_ram__max'], game_data['rec_storage__max']

        # programrequirement view(각 프로그램에 대한 cpu,gpu 요구량 및 ram , 등을 정리한 view)에서 사용자가 입력한 프로그램 리스트중에서 가장 높은 사양을 뽑는다.
        program_data = ProgramRequirements.objects.filter(name__in=programs).aggregate(
            Max('rec_cpu_point'), Max('rec_gpu_point'), Max('rec_ram'))
        program_cpu_point, program_gpu_point, program_ram = program_data[
            'rec_cpu_point__max'], program_data['rec_gpu_point__max'], program_data['rec_ram__max']
        
        # cpu_point, gpu_point, ram, storage를 선택된 게임, 프로그램에 맞춘다.
        queryset = LaptopPerformance.objects.filter(cpu_point__gte=comparator(game_cpu_point, program_cpu_point), gpu_point__gte=comparator(game_gpu_point, program_gpu_point),
                                                    ram__gte=comparator(game_ram, program_ram)//2, price__lte=budget)

        if game_storage is not None:
            queryset = queryset.filter(
                Q(ssd__gte=game_storage) | Q(hdd__gte=game_storage))
        
        # 실외 작업용인 경우에대한 처리
        if outdoor == True:
            # 가방 종류에 따라 무게 제한 처리
            if bag == "eco-bag":
                queryset = queryset.filter(weight__lte=1.4)
            elif bag == "cross-bag":
                queryset = queryset.filter(weight__lte=1.8)
            elif bag == "hand-bag":
                queryset = queryset.filter(weight__lte=1.0)
            elif bag == "briefcase":
                queryset = queryset.filter(weight__lte=1.0)
            elif bag == "backpag":
                queryset = queryset.filter(weight__lte=2.0)
        
        # 최종 결과에 대한 필터링 기준에 맞게 정렬또는 처리를 진행한다.
        if priority == "performance-first":
            queryset = queryset.order_by(
                'cpu_point', 'gpu_point', 'ram', 'resolution', 'display', 'ssd', 'hdd').reverse()
        elif priority == "price-first":
            queryset = queryset.order_by('price')
        elif priority == "service-first":
            queryset = queryset.filter(Q(name__startswith='삼성') | Q(name__startswith='LG') | Q(
                name__startswith='애플') | Q(name__startswith='마이크로소프트'))
        

        # 최대 10개의 노트북 리스틑 출력한다.
        if len(queryset) > 10:
            queryset = queryset.all()[:10]
        serializer = LaptopPerformanceSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        print('LOG:GET')
