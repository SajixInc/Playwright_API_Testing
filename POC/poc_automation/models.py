from django.db import models


class InputModel(models.Model):
    DoesNotExist = None
    url = models.CharField(max_length=1000)
    method = models.CharField(max_length=1000)
    headers = models.CharField(max_length=1000)
    payload = models.CharField(max_length=1000)
    staging_version = models.CharField(max_length=1000)
    EnvironmentName = models.CharField(max_length=1000)
    Testcase_Version = models.CharField(max_length=1000)
    Project_Name = models.CharField(max_length=1000)
    Test = models.CharField(max_length=1000)
    objects = models.Manager()

    class Meta:
        db_table = 'Poc_Input_IvinPro'


class lifeeazyModel(models.Model):
    DoesNotExist = None
    url = models.CharField(max_length=1000)
    method = models.CharField(max_length=1000)
    headers = models.CharField(max_length=1000)
    payload = models.CharField(max_length=1000)
    staging_version = models.CharField(max_length=1000)
    EnvironmentName = models.CharField(max_length=1000)
    Testcase_Version = models.CharField(max_length=1000)
    Project_Name = models.CharField(max_length=1000)
    Test = models.CharField(max_length=1000)
    objects = models.Manager()

    class Meta:
        db_table = 'Poc_Input_Lifeeazy'
