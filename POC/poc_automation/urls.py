from .views import *
from django.urls import path
from .views import IvinExcelUpload, Ivingetall, IvinProjectname, IvinProject, IvinUpdate, IvinDelete, lifeeazyExcelUpload, lifeeazygetall, lifeeazyProjectname,lifeeazygetproject
# from .test_excel import objects

urlpatterns = [
    path('post/', IvinExcelUpload.as_view(), name='ivin upload'),
    path('getall/', Ivingetall.as_view(), name='getall ivin details'),
    path('project/<str:Project_Name>', IvinProjectname.as_view(), name='project-name'),
    path('projectname/', IvinProject.as_view(), name='projectname'),
    path('put/<int:pk>', IvinUpdate.as_view(), name='update'),
    path('delete/<int:pk>', IvinDelete.as_view(), name='delete'),
    path('lifepost/', lifeeazyExcelUpload.as_view(), name='lifeeazy-data'),
    path('lifegetall/', lifeeazygetall.as_view(), name='lifeeazy-getall'),
    path('lifeget/<str:Project_Name>', lifeeazyProjectname.as_view(), name='lifeeazy-projectname'),
    path('lifegetproject/', lifeeazygetproject.as_view(), name='projectname'),
    # path('object/<str:method>/',objects.as_view())
]

