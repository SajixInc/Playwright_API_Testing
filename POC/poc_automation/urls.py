from .views import *
from django.urls import path
from .views import IvinExcelUpload, Ivingetall, IvinProjectname, IvinProject, IvinUpdate, IvinDelete, lifeeazyExcelUpload, lifeeazygetall, lifeeazyProjectname,lifeeazygetproject
# from .test_excel import objects

urlpatterns = [
    path('upload/', IvinExcelUpload.as_view(), name='ivin upload'),
    path('getalldetails/', Ivingetall.as_view(), name='getall ivin details'),
    path('projectname/<str:Project_Name>', IvinProjectname.as_view(), name='project-name'),
    path('project/', IvinProject.as_view(), name='projectname'),
    path('put/<int:pk>', IvinUpdate.as_view(), name='update'),
    path('delete/<int:pk>', IvinDelete.as_view(), name='delete'),
    path('post/', lifeeazyExcelUpload.as_view(), name='lifeeazy-data'),
    path('getall/', lifeeazygetall.as_view(), name='lifeeazy-getall'),
    path('pname/<str:Project_Name>', lifeeazyProjectname.as_view(), name='lifeeazy-projectname'),
    path('getprojectname/', lifeeazygetproject.as_view(), name='projectname'),
    # path('object/<str:method>/',objects.as_view())
]

