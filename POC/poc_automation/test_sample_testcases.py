
import json
import pymongo
import requests
import pytest
from playwright.sync_api import APIRequestContext, Playwright
from typing import Generator
import datetime
from pymongo import MongoClient
DateTime = datetime.datetime.now()
import json
from database import x

username = x['default']
a = x['default']['NAME']
try:
    y = x['default']['CLIENT']
    myclient = pymongo.MongoClient(
        f"mongodb://{username['CLIENT']['username']}:{username['CLIENT']['password']}@{username['CLIENT']['host']}:27017/")
except:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[a]
collection1 = mydb["Output_FirstData"]
collection2 = mydb["Output_SecondData"]

client = MongoClient('mongodb://localhost:27017/')
db = client['poc']
results_collection1 = db['Input_LifeeazyData']
results_collection2 = db['Input_IvinProData']
def get1_entries():
    c = results_collection1.find().sort("_id", -1).limit(8)
    entries = []
    for i in c:
        entries.append(i)
    print(len(entries), "entries")
    return entries

def get2_entries():
    k = results_collection2.find().sort("_id", -1).limit(6)
    entries = []
    for j in k:
        entries.append(j)
    print(len(entries), "entries")
    return entries
@pytest.fixture(scope="session")
def api_lifeeazy(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url="http://staging-api.vivifyhealthcare.com/")
    global list1
    list1 = get1_entries()
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session")
def api_ivin(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url="http://172.105.37.117:8000/")
    global list2
    list2 = get2_entries()
    yield request_context
    request_context.dispose()



def test_getalergies(api_lifeeazy: APIRequestContext) -> None:
    ac = list1
    for values in ac:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'GET' and Test == 'Allergiesbyuserid Get':
            cleaned_string = url.replace("\u200B", "")
            get_todo = api_lifeeazy.get(url=str(cleaned_string), headers=headers23)
            try:
                test1 = get_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "5",
                            "Pre condition": "Allergies data based on Userid",
                            "Flow ": "Get",
                            "App Name": "Lifeeazy",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    if values in list1:
                        list1.remove(values)
                        print(len(list1))
                    for j in list1:
                        print(j['url'])
                else:
                    data = {"Test Case-Id": "5",
                            "Pre condition": "Enter the correct userid",
                            "Flow ": "Get",
                            "App Name": "Lifeeazy",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    if values in list1:
                        list1.remove(values)
                        print(len(list1))
                    for j in list1:
                        print(j['url'])
            except Exception as e:
                data = {"Test Case-Id": "5",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Get",
                        "App Name": "Lifeeazy",
                        "Expected Output": '404',
                        "Actual Output": str(get_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection1.insert_one(data)
                if values in list1:
                    list1.remove(values)
                    print(len(list1))
                for j in list1:
                    print(j['url'])
            assert get_todo.ok

def test_example(api_lifeeazy: APIRequestContext) -> None:
    ac = list1
    for values in ac:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'GET' and Test == 'Anthropometricsbyfamilyid Get':
            cleaned_string = url.replace("\u200B", "")
            get_todo = api_lifeeazy.get(url=str(cleaned_string), headers=headers23)
            try:
                test1 = get_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "6",
                            "Pre condition": "Get the Anthropometric data based on FamilyId",
                            "Flow ": "Get",
                            "App Name": "Lifeeazy",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    if values in list1:
                        list1.remove(values)
                        print(len(list1))
                    for j in list1:
                        print(j['url'])
                else:
                    data = {"Test Case-Id": "6",
                            "Pre condition": "Enter the correct familyid",
                            "Flow ": "Get",
                            "App Name": "Lifeeazy",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    if values in list1:
                        list1.remove(values)
                        print(len(list1))
                    for j in list1:
                        print(j['url'])
            except Exception as e:
                data = {"Test Case-Id": "6",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Get",
                        "App Name": "Lifeeazy",
                        "Expected Output": '404',
                        "Actual Output": str(get_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection1.insert_one(data)
                if values in list1:
                    list1.remove(values)
                    print(len(list1),)
                for j in list1:
                    print(j['url'])
            assert get_todo.ok

def test_lifeeazypost(api_lifeeazy: APIRequestContext) -> None:
    ab = list1
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'POST' and Test == 'Allergies Post':
            cleaned_string = url.replace("\u200B", "")
            post_todo = api_lifeeazy.post(url=str(cleaned_string), headers=headers23, data=payload)
            try:
                test1 = post_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "1",
                            "Pre condition": "Post",
                            "Flow ": "Post Register",
                            "App Name": "Lifeeazy",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            "TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            "TestCase Version": Testcase_Version,
                            "Project Name": Project_Name}
                    collection1.insert_one(data)
                    # if values in list1:
                    #     list1.remove(values)
                    #     print(len(list1), "mani")
                    # for j in list1:
                    #     print(j['url'])
                else:
                    data = {"Test Case-Id": "1",
                            "Pre condition": "Enter the valid details",
                            "Flow ": "Post Register",
                            "App Name": "Lifeeazy",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    # if values in list1:
                    #     list1.remove(values)
                    #     print(len(list1),"mani")
                    # for j in list1:
                    #     print(j['url'])

            except Exception as e:
                data = {"Test Case-Id": "1",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Post Register",
                        "App Name": "Lifeeazy",
                        "Expected Output": '404',
                        "Actual Output": str(post_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection1.insert_one(data)
                # if values in list1:
                #     list1.remove(values)
                #     print(len(list1), "mani")
                # for j in list1:
                #     print(j['url'])
            assert post_todo.ok

def test_lifeeazyget(api_lifeeazy: APIRequestContext) -> None:
    ab = list1
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'GET' and Test == 'Allergies Get':
            cleaned_string = url.replace("\u200B", "")
            get_todo = api_lifeeazy.get(url=str(cleaned_string), headers=headers23)
            # assert get_todo.ok
            # p = get_todo.json()
            # print(p)
            try:
                test1 = get_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "2",
                            "Pre condition": "Get All The Alergies Data",
                            "Flow ": "Getall data",
                            "App Name": "Lifeeazy",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    # if values in list1:
                    #     list1.remove(values)
                    #     print(len(list1), "mani")
                    # for j in list1:
                    #     print(j['url'])
                else:
                    data = {"Test Case-Id": "2",
                            "Pre condition": "Get All The Alergies Data",
                            "Flow ": "Getall data",
                            "App Name": "Lifeeazy",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    # if values in list1:
                    #     list1.remove(values)
                    #     print(len(list1), "mani")
                    # for j in list1:
                    #     print(j['url'])
            except Exception as e:
                data = {"Test Case-Id": "2",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Getall data",
                        "App Name": "Lifeeazy",
                        "Expected Output": '404',
                        "Actual Output": str(get_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection1.insert_one(data)
                # if values in list1:
                #     list1.remove(values)
                #     print(len(list1), "mani")
                # for j in list1:
                #     print(j['url'])
            assert get_todo.ok

def test_lifeeazyupdate(api_lifeeazy: APIRequestContext) -> None:
    ab = list1
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'PUT' and Test == 'Address Put':
            cleaned_string = url.replace("\u200B", "")
            put_todo = api_lifeeazy.put(url=str(cleaned_string), headers=headers23, data=payload)
            try:
                test1 = put_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "3",
                            "Pre condition": "Updating Vitals by using VitalsId",
                            "Flow ": "Update Vitals",
                            "App Name": "Lifeeazy",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    # if values in list1:
                    #     list1.remove(values)
                    #     print(len(list1), "mani")
                    # for j in list1:
                    #     print(j['url'])
                else:
                    data = {"Test Case-Id": "3",
                            "Pre condition": "Enter the valid details",
                            "Flow ": "Update Vitals",
                            "App Name": "Lifeeazy",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    # if values in list1:
                    #     list1.remove(values)
                    #     print(len(list1), "mani")
                    # for j in list1:
                    #     print(j['url'])
            except Exception as e:
                data = {"Test Case-Id": "3",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Update Vitals",
                        "App Name": "Lifeeazy",
                        "Expected Output": '404',
                        "Actual Output": str(put_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection1.insert_one(data)
                # if values in list1:
                #     list1.remove(values)
                #     print(len(list1), "mani")
                # for j in list1:
                #     print(j['url'])
            assert put_todo.ok

def test_lifeeazydelete(api_lifeeazy: APIRequestContext) -> None:
    ab = list1
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'DELETE' and Test == 'User Delete':
            cleaned_string = url.replace("\u200B", "")
            delete_todo = api_lifeeazy.delete(url=str(cleaned_string), headers=headers23, data=payload)
            try:
                test1 = delete_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "4",
                            "Pre condition": "We can delete User by using UserId(id)",
                            "Flow ": "Delete User details",
                            "App Name": "Lifeeazy",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    # if values in list1:
                    #     list1.remove(values)
                    #     print(len(list1), "mani")
                    # for j in list1:
                    #     print(j['url'])
                else:
                    data = {"Test Case-Id": "4",
                            "Pre condition": "Enter the valid id",
                            "Flow ": "Delete User details",
                            "App Name": "Lifeeazy",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    # if values in list1:
                    #     list1.remove(values)
                    #     print(len(list1), "mani")
                    # for j in list1:
                    #     print(j['url'])
            except Exception as e:
                data = {"Test Case-Id": "4",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Delete User details",
                        "App Name": "Lifeeazy",
                        "Expected Output": '404',
                        "Actual Output": str(delete_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection1.insert_one(data)
                # if values in list1:
                #     list1.remove(values)
                #     print(len(list1), "mani")
                # for j in list1:
                #     print(j['url'])
            assert delete_todo.ok

def test_example1(api_lifeeazy: APIRequestContext) -> None:
    ac = list1
    for values in ac:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'GET' and Test == 'Anthropometricsbyuserid Get':
            cleaned_string = url.replace("\u200B", "")
            get_todo = api_lifeeazy.get(url=str(cleaned_string), headers=headers23)
            try:
                test1 = get_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "7",
                            "Pre condition": "Get the Anthropometric data based on UserId",
                            "Flow ": "Get",
                            "App Name": "Lifeeazy",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    if values in list1:
                        list1.remove(values)
                        print(len(list1))
                    for j in list1:
                        print(j['url'])
                else:
                    data = {"Test Case-Id": "7",
                            "Pre condition": "Enter the correct userid",
                            "Flow ": "Get",
                            "App Name": "Lifeeazy",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    if values in list1:
                        list1.remove(values)
                        print(len(list1))
                    for j in list1:
                        print(j['url'])
            except Exception as e:
                data = {"Test Case-Id": "7",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Get",
                        "App Name": "Lifeeazy",
                        "Expected Output": '404',
                        "Actual Output": str(get_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection1.insert_one(data)
                if values in list1:
                    list1.remove(values)
                    print(len(list1))
                for j in list1:
                    print(j['url'])
            assert get_todo.ok

def test_example2(api_lifeeazy: APIRequestContext) -> None:
    ac = list1
    for values in ac:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'GET' and Test == 'Lablevelbyfamilyid Get':
            cleaned_string = url.replace("\u200B", "")
            get_todo = api_lifeeazy.get(url=str(cleaned_string), headers=headers23)
            try:
                test1 = get_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "8",
                            "Pre condition": "Lablevel details of family member by using familyid",
                            "Flow ": "Get",
                            "App Name": "Lifeeazy",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    if values in list1:
                        list1.remove(values)
                        print(len(list1))
                    for j in list1:
                        print(j['url'])
                else:
                    data = {"Test Case-Id": "8",
                            "Pre condition": "Enter the correct familyid",
                            "Flow ": "Get",
                            "App Name": "Lifeeazy",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection1.insert_one(data)
                    if values in list1:
                        list1.remove(values)
                        print(len(list1))
                    for j in list1:
                        print(j['url'])
            except Exception as e:
                data = {"Test Case-Id": "8",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Get",
                        "App Name": "Lifeeazy",
                        "Expected Output": '404',
                        "Actual Output": str(get_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection1.insert_one(data)
                if values in list1:
                    list1.remove(values)
                    print(len(list1))
                for j in list1:
                    print(j['url'])
            assert get_todo.ok

def test_ivinpost(api_ivin: APIRequestContext) -> None:
    ab = list2
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'POST' and Test == 'Spost':
            cleaned_string = url.replace("\u200B", "")
            post_todo = api_ivin.post(url=str(cleaned_string), headers=headers23, data=payload)
            try:
                test1 = post_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "1",
                            "Pre condition": "Add the candidate profile for social media view",
                            "Flow ": "SociaMedia Post",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "Candidate_Profile",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
                else:
                    data = {"Test Case-Id": "1",
                            "Pre condition": "Add the candidate profile for social media view",
                            "Flow ": "SociaMedia Post",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "Candidate_Profile",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
            except Exception as e:
                data = {"Test Case-Id": "1",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "SociaMedia Post",
                        "App Name": "Ivin_Pro",
                        "Expected Output": '404',
                        "Actual Output": str(post_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "Candidate_Profile",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection2.insert_one(data)
            assert post_todo.ok

def test_ivinget(api_ivin: APIRequestContext) -> None:
    ab = list2
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'GET' and Test == 'Sgetall':
            cleaned_string = url.replace("\u200B", "")
            get_todo = api_ivin.get(url=str(cleaned_string), headers=headers23)
            try:
                test1 = get_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "2",
                            "Pre condition": "Get all the Social media details",
                            "Flow ": "Getall data",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "Candidate_Profile",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
                else:
                    data = {"Test Case-Id": "2",
                            "Pre condition": "Enter the valid details",
                            "Flow ": "Getall data",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "Candidate_Profile",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
            except Exception as e:
                data = {"Test Case-Id": "2",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Getall data",
                        "App Name": "Ivin_Pro",
                        "Expected Output": '404',
                        "Actual Output": str(get_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "Candidate_Profile",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection2.insert_one(data)
            assert get_todo.ok

def test_ivinupdate(api_ivin: APIRequestContext) -> None:
    ab = list2
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'PUT' and Test == 'Sput':
            cleaned_string = url.replace("\u200B", "")
            put_todo = api_ivin.put(url=str(cleaned_string), headers=headers23, data=payload)
            try:
                test1 = put_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "3",
                            "Pre condition": "Updating Social media by using candidate profileid",
                            "Flow ": "Update",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "Candidate_Profile",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
                else:
                    data = {"Test Case-Id": "3",
                            "Pre condition": "Enter the valid details",
                            "Flow ": "Update SocialMedia",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "Candidate_Profile",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
            except Exception as e:
                data = {"Test Case-Id": "3",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Update",
                        "App Name": "Ivin_Pro",
                        "Expected Output": '404',
                        "Actual Output": str(put_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "Candidate_Profile",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection2.insert_one(data)
            assert put_todo.ok

def test_ivindelete(api_ivin: APIRequestContext) -> None:
    ab = list2
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'DELETE' and Test == 'Sdelete':
            cleaned_string = url.replace("\u200B", "")
            delete_todo = api_ivin.delete(url=str(cleaned_string), headers=headers23, data=payload)
            try:
                test1 = delete_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "4",
                            "Pre condition": "Delete the Social media for particular candidate profileid",
                            "Flow ": "Delete method",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "Candidate_Profile",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
                else:
                    data = {"Test Case-Id": "4",
                            "Pre condition": "Enter the valid id",
                            "Flow ": "Delete method",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "Candidate_Profile",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
            except Exception as e:
                data = {"Test Case-Id": "4",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Delete method",
                        "App Name": "Ivin_Pro",
                        "Expected Output": '404',
                        "Actual Output": str(delete_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "Candidate_Profile",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection2.insert_one(data)
            assert delete_todo.ok

def test_ivingetall(api_ivin: APIRequestContext) -> None:
    ab = list2
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'GET' and Test == 'Getall StateNames':
            cleaned_string = url.replace("\u200B", "")
            get_todo = api_ivin.get(url=str(cleaned_string), headers=headers23)
            try:
                test1 = get_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "5",
                            "Pre condition": "Get all the StateNames",
                            "Flow ": "Getall data",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User-Ivin",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
                else:
                    data = {"Test Case-Id": "5",
                            "Pre condition": "Enter the valid details",
                            "Flow ": "Getall data",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User-Ivin",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
            except Exception as e:
                data = {"Test Case-Id": "5",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Getall data",
                        "App Name": "Ivin_Pro",
                        "Expected Output": '404',
                        "Actual Output": str(get_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User-Ivin",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection2.insert_one(data)
            assert get_todo.ok

def test_ivingetall1(api_ivin: APIRequestContext) -> None:
    ab = list2
    for values in ab:
        url = values['url']
        method = values['method']
        headers = values['headers']
        payload = values['payload']
        staging_version = values['staging_version']
        EnvironmentName = values['EnvironmentName']
        Testcase_Version = values['Testcase_Version']
        Project_Name = values['Project_Name']
        Test = values['Test']
        headers23 = {'Content-Type': 'application/json', 'Authorization': f"Bearer {headers}"}
        if method == 'GET' and Test == 'Getall Workers':
            cleaned_string = url.replace("\u200B", "")
            get_todo = api_ivin.get(url=str(cleaned_string), headers=headers23)
            try:
                test1 = get_todo.json()
                if test1['Status'] == 200:
                    data = {"Test Case-Id": "6",
                            "Pre condition": "Get all the Workers",
                            "Flow ": "Getall data",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "200",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User-Ivin",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Success",
                            " TestCase Status API": "Pass TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
                else:
                    data = {"Test Case-Id": "6",
                            "Pre condition": "Enter the valid details",
                            "Flow ": "Getall data",
                            "App Name": "Ivin_Pro",
                            "Expected Output": "400",
                            "Actual Output": str(test1),
                            "Endpoint Name": str(url),
                            "Section Name": "User-Ivin",
                            "API Type": "User",
                            "Status Code": test1['Status'],
                            "Status": "Fail",
                            " TestCase Status API": "Fail TestCase",
                            "Test Run Date": DateTime,
                            "Test Releated To Version": str(staging_version),
                            'Environment Name': EnvironmentName,
                            'TestCase Version': Testcase_Version,
                            'Project Name': Project_Name}
                    collection2.insert_one(data)
            except Exception as e:
                data = {"Test Case-Id": "6",
                        "Pre condition": "Give the correct url&data",
                        "Flow ": "Getall data",
                        "App Name": "Ivin_Pro",
                        "Expected Output": '404',
                        "Actual Output": str(get_todo),
                        "Endpoint Name": str(url),
                        "Section Name": "User-Ivin",
                        "API Type": "User",
                        "Status Code": 404,
                        "Status": "Not Found",
                        " TestCase Status API": "Fail TestCase",
                        "Test Run Date": DateTime,
                        "Test Releated To Version": str(staging_version),
                        'Environment Name': EnvironmentName,
                        'TestCase Version': Testcase_Version,
                        'Project Name': Project_Name}
                collection2.insert_one(data)
            assert get_todo.ok
