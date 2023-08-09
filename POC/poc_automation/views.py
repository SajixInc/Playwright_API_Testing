from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from rest_framework.generics import GenericAPIView
import pandas as pd
from .models import *


class IvinExcelUpload(GenericAPIView):
    serializer_class = IvinSerializer

    def post(self, request):
        df = pd.read_excel(r'F:\poc-automatica\POC\poc_automation\testcases_Ivin.xlsx')

        rows = df.to_dict(orient='records')

        serializer = IvinSerializer(data=rows, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response("IvinPro Upload Successfully")
        else:
            return Response(serializer.errors, status=400)


class Ivingetall(APIView):
    def get(self, request):
        queryset = InputModel.objects.all()
        serializer = IvinSerializer(queryset, many=True)
        return Response(serializer.data)


class IvinProjectname(generics.GenericAPIView):
    queryset = IvinProjectSerializer
    def get(self, request, Project_Name):
        project_name = InputModel.objects.filter(Project_Name=Project_Name)
        serializer = IvinProjectSerializer(project_name,many=True)
        return Response(serializer.data)


class IvinProject(generics.GenericAPIView):
    serializer_class = IvinProjectSerializer
    def post(self, request):
        projectname = request.data.get("Project_Name")
        # print(projectname)
        # PlayWright1(projectname)
        return Response('Done')


class IvinUpdate(generics.GenericAPIView):
    serializer_class = IvinProjectSerializer
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
    serializer_class = IvinProjectSerializer
    def delete(self, request, pk):
        try:
            instance = InputModel.objects.get(pk=pk)
        except InputModel.DoesNotExist:
            return Response("Record not found", status=404)
        instance.delete()
        return Response("Record deleted successfully")



class lifeeazyExcelUpload(GenericAPIView):
    serializer_class = lifeeazySerializer
    def post(self, request):
        df = pd.read_excel(r'F:\poc-automatica\POC\poc_automation\testcases_lifeeazy.xlsx')

        rows = df.to_dict(orient='records')

        serializer = lifeeazySerializer(data=rows, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Lifeeazy Upload Successfully")
        else:
            return Response(serializer.errors, status=400)


class lifeeazygetall(APIView):

    def get(self, request):
        queryset = lifeeazyModel.objects.all()
        serializer_class = lifeeazySerializer(queryset, many=True)# Add the queryset attribute here
        return Response(serializer_class.data)

class lifeeazyProjectname(generics.GenericAPIView):
    queryset = lifeeazyProjectSerializer

    def get(self, request, Project_Name):
        project_name = lifeeazyModel.objects.filter(Project_Name=Project_Name)
        serializer = lifeeazyProjectSerializer(project_name,many=True)
        return Response(serializer.data)


class lifeeazygetproject(generics.GenericAPIView):
    serializer_class = lifeeazyProjectSerializer
    def post(self, request):
        projectname = request.data.get("Project_Name")
        # print(projectname)
        # PlayWright1(projectname)
        return Response('Done lifeeazy')


class lifeeazyUpdate(generics.GenericAPIView):
    serializer_class = lifeeazySerializer
    def put(self, request, pk):
        try:
            instance = lifeeazyModel.objects.get(pk=pk)
        except lifeeazyModel.DoesNotExist:
            return Response("Record not found", status=404)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Update the records")

class lifeeazyDelete(generics.GenericAPIView):
    serializer_class = lifeeazySerializer
    def delete(self, request, pk):
        try:
            instance = lifeeazyModel.objects.get(pk=pk)
        except lifeeazyModel.DoesNotExist:
            return Response("Record not found", status=404)
        instance.delete()
        return Response("Record deleted successfully")
