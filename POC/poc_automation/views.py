from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import MyModelSerializer,MydataSerializer, ProjectSerializer, lifeSerializer, lifeeazySerializer
from rest_framework.generics import GenericAPIView
import pandas as pd
from .models import *


class IvinExcelUpload(GenericAPIView):
    serializer_class = MyModelSerializer

    def post(self, request):
        df = pd.read_excel(r'F:\poc-automatica\POC\poc_automation\testcases_Ivin.xlsx')

        rows = df.to_dict(orient='records')

        serializer = MyModelSerializer(data=rows, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Data uploaded successfully")
        else:
            return Response(serializer.errors, status=400)


class Ivingetall(APIView):
    def get(self, request):
        queryset = InputModel.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)


class IvinProjectname(generics.GenericAPIView):
    queryset = MydataSerializer

    def get(self, request, Project_Name):
        project_name = InputModel.objects.filter(Project_Name=Project_Name)
        serializer = MydataSerializer(project_name,many=True)
        return Response(serializer.data)


class IvinProject(generics.GenericAPIView):
    serializer_class = ProjectSerializer
    def post(self, request):
        projectname = request.data.get("Project_Name")
        # print(projectname)
        # PlayWright1(projectname)
        return Response('Done')


class IvinUpdate(generics.GenericAPIView):
    serializer_class = ProjectSerializer
    def put(self, request, pk):
        try:
            instance = InputModel.objects.get(pk=pk)
        except InputModel.DoesNotExist:
            return Response("Record not found", status=404)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Record updated successfully")

class IvinDelete(generics.GenericAPIView):
    serializer_class = ProjectSerializer
    def delete(self, request, pk):
        try:
            instance = InputModel.objects.get(pk=pk)
        except InputModel.DoesNotExist:
            return Response("Record not found", status=404)
        instance.delete()
        return Response("Record deleted successfully")



class lifeeazyExcelUpload(GenericAPIView):
    serializer_class = lifeSerializer
    def post(self, request):
        df = pd.read_excel(r'F:\poc-automatica\POC\poc_automation\testcases_lifeeazy.xlsx')

        rows = df.to_dict(orient='records')

        serializer = lifeSerializer(data=rows, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Upload successful")
        else:
            return Response(serializer.errors, status=400)


class lifeeazygetall(APIView):

    def get(self, request):
        queryset = lifeeazyModel.object.all()
        serializer_class = lifeSerializer(queryset, many=True)# Add the queryset attribute here
        return Response(serializer_class.data)

class lifeeazyProjectname(generics.GenericAPIView):
    queryset = lifeSerializer

    def get(self, request, Project_Name):
        project_name = lifeeazyModel.object.filter(Project_Name=Project_Name)
        serializer = lifeSerializer(project_name,many=True)
        return Response(serializer.data)


class lifeeazygetproject(generics.GenericAPIView):
    serializer_class = lifeeazySerializer
    def post(self, request):
        projectname = request.data.get("Project_Name")
        # print(projectname)
        # PlayWright1(projectname)
        return Response('Done lifeeazy')


