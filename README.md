
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png" align="right" width="250"/> <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*gMiUPuRGC36nxZHe2zthOg.png" width="180"/> 

<h1 font-size="50px" align="center">API Testing Via Playwright Using Python</h1>

Playwright is a opensource framework that provides a high-level capability to enable automation testing. It also allows you to write scripts in Python that can control web browsers and perform various tasks such as filling out forms, clicking buttons, navigating pages, and taking screenshots.

Playwright offers several advantages over other browser automation tools:
- It supports multiple browsers, which means you can test your web application on different browsers using the same script.
- It has a simple and intuitive API that makes it easy to use even for beginners.
- It provides better performance and reliability compared to other tools.
In summary, Playwright is a powerful and flexible tool for automating web browsers in Python, and it can be used for a wide range of tasks such as testing, web scraping, and web automation.

Playwright enables automation of web browsers (including Chrome, Firefox, and Safari) for end-to-end testing of web applications. While Playwright is primarily designed to be used with JavaScript, it is possible to use it with Python as well by using the py_playwright library, which provides a Python API for Playwright.

# How to Installation :

Install Playwright and its dependencies using pip:

    pip install playwright
    playwright install

# Example Test :

Create a test_playwright.py file inside the current working directory or in a sub-directory with the code below:

    import re
    from playwright.sync_api import Page, expect


    def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))
 
# Running the Example Test :

By default tests will be run on chromium. This can be configured via the CLI options. Tests are run in headless mode meaning no browser UI will open up when running the tests. Results of the tests and test logs will be shown in the terminal.

    pytest

# How to use Playwright for API testing :

Playwright can be used to get access to the REST API of your application.

Sometimes you may want to send requests to the server directly from Python without loading a page and running js code in it. A few examples where it may come in handy:

* Test your server API.
* Prepare server side state before visiting the web application in a test.
* Validate server side post-conditions after running some actions in the browser.
All of that could be achieved via APIRequestContext methods.

# Writing API Test :

APIRequestContext can send all kinds of HTTP(S) requests over network.

The following example demonstrates how to use Playwright to test issues creation via GitHub API. The test suite will do the following:

* Create a new repository before running tests.
* Create a few issues and validate server state.
* Delete the repository after running tests.

# Configure :

In our case; VivifyHealthCare API requires authorization, so we can configure the token once for all tests. While at it, we'll also set the baseURL to simplify the tests. below example set is without JWT authentication.

    import pytest
    from playwright.sync_api import Playwright, APIRequestContext
    from typing import Generator

    @pytest.fixture(scope="session")

    def api_request_context(
    playwright: Playwright,
    )-> Generator[APIRequestContext,None,None]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


# Write tests :
Now that we initialized request object we can add a few tests

# Post :

    from playwright.sync_api import Playwright,APIRequestContext


    def test_post_example(api_request_context: APIRequestContext) -> None:
    headers = {"Content-type": "application/json"}
    data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
    }
    post_todo = api_request_context.post(
    f"https://jsonplaceholder.typicode.com/posts", data=data, headers=headers
    )
    # assert post_todo.ok
    assert post_todo.json()["title"] == "foo"

# Get :
    def test_get_example(api_request_context: APIRequestContext:
    headers = {"Content-type": "application/json"}
    get_todo = api_request_context.get(
    f"https://jsonplaceholder.typicode.com/posts/1",  headers=headers
    )
    assert get_todo.ok

# Put (Update):
    
    def test_put_example(api_request_context: APIRequestContext:
    headers = {"Content-type": "application/json"}
    data = {
    "title": "foo2",
    "body": "bar",
    "userId": 1
    }
    put_todo = api_request_context.put(
    f"https://jsonplaceholder.typicode.com/posts/1", data=data, headers=headers
    )
    assert put_todo.ok
    assert put_todo.status == 200
    assert put_todo.json()["title"] == "foo2"

# Delete :

    def test_delete_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    delete_todo = api_request_context.delete(
    f"https://jsonplaceholder.typicode.com/posts/1", headers=headers)
    assert delete_todo.ok
    assert delete_todo.status == 200

# To Run :

To run this script, need to be in directory and run the following command :

    pytest

# Results :

<img src = "https://user-images.githubusercontent.com/109729440/223346253-23cd14b2-0d39-40d9-88b9-5010d3bd9dfc.png" width=1000>


<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>

Tech-Stack provides a space for discussions on a variety of topics including product reviews, software development, and emerging technologies. Join our community, simply click on the invitation link below and follow the prompts to create your account. We look forward to welcoming you to our community!       

<img src="https://blogs.vivifyhealthcare.com/wp-content/uploads/2023/03/Discord-1.png" margin_left="100"/>  

[Invitation link](https://lnkd.in/gmkMQnZD)
  ....

