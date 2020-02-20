from django.urls import path, include
from fp_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cpus',views.CpuViewSet)
router.register('gpus',views.GpuViewSet)
router.register('laptops',views.LaptopViewSet)
router.register('games',views.GameViewSet)
router.register('programs',views.ProgramViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('asdfasdf/', views.asdfasdf, exampleparameter='wfeefsdf')
]
