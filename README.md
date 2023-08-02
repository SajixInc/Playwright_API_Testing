<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png" align="right" width="250"/> <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*gMiUPuRGC36nxZHe2zthOg.png" width="145"/> 

<h1 font-size="50px" align="center">Multiple TestCases for Multiple Products</h1>


Python-based API testing and automation tool that allows testers and developers to efficiently organize, execute, and manage test cases for multiple projects or products. The project utilizes Django as the web framework and MongoDB as the backend database for seamless data storage.
It offers a user-friendly interface for grouping API collections by product (e.g.,Lifeeazy and IvinPro) and uploading test cases for each product.The tool automates the execution of test cases, captures the data, and stores the results in MongoDB.


# Prerequisites:
   
* Install Python and MonogoDB on your system.

* Install Playwright:
  
      pip install playwright   
      playwright install

* Install necessary dependencies:
  
      pip install pytest
      pip install playwright
      pip install requests

# Setup your project:

* Create a new project directory

* Inside the project directory, create a virtual environment (optional but recommended) by running:
  
        python -m venv venv

* Activate the virtual environment:
  - On Windows:

        venv\Scripts\activate
  - On macOS/Linux:

        source venv/bin/activate

* Configure the MongoDB connection settings in the Django settings file.

* Django project with the required components (models, serializers, views, and URLs) to handle API requests.

# Excel Test Cases:

* Create an Excel document containing test cases for both the "Lifeeazy" and "Ivinpro" APIs.

* Organize the test cases with details such as API endpoints, request payloads, status, status_code, method, testcase_version, expected responses, etc.

<img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+(103).png" width=800>

# Uploading Test Cases via API:

* Write a view function that reads the test cases from the Excel document for both "Lifeeazy" and "Ivinpro" APIs.

* Create API endpoints to allow users to upload test cases for API collections.

* Use a library like pandas to parse the Excel file and extract the relevant information.

* Accept test case data in a standardized format, including API endpoints, request payloads, and expected responses, etc.

* To run the command in the Terminal:

        python manage.py runserver

<img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+(101).png" width=600>

# Saving Test Cases to MongoDB:

* In the views function, process the uploaded test cases and save them to separate MongoDB collections for each product.

* For example, save the Lifeeazy test cases to the "lifeeazy_test_cases" collection and the IvinPro test cases to the "ivinpro_test_cases" collection.

# Writing Playwright Test Cases:

* Once the data is saved in MongoDB, you might perform API testing.

* Utilize Playwright to write test cases for each product's APIs separately (e.g., Lifeeazy and IVINPro).

    - Send a specific request to the endpoint (e.g., GET, POST, PUT, DELETE) with the necessary parameters.
  - Capture and validate the response received from the API endpoint.

* Ensure that each Playwright test case corresponds to a specific API endpoint and captures the relevant response data.

# Test Case Execution:  
  
* Execute the Playwright test cases for both "Lifeeazy" and "Ivinpro" APIs.

* To run this script, need to be in directory and run the following command :

         pytest --template=html1/index.html --report=report.html 

# Saving Test Results to MongoDB:

* After executing the test cases, save the test results and captured data to separate MongoDB collections for each product.

* For instance, store the Lifeeazy test results in the "Lifeeazy_test_results" collection and the IvinPro test results in the "IvinPro_test_results" collection.

# Results:

<img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Screenshot+(99).png" width=700>

<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>





