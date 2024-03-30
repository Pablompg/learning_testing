# exercise 4. Testing simple apis using mocks and a fake database.

In this exercise we are going to have a very simple api with only one endpoint for authenticating a user.
Our aim is to test the endpoint by mocking the database

The api is built with fastapi and uvicorn. It uses sqlalchemy as an ORM. For testing we use pytest.

# Requirements
* Have python 3.11 or higher installed
* Have poetry installed

# Instructions
* `poetry install` to install dependencies
* `poetry run pytest` to execute the test suite
* `poetry run uvicorn main:app --reload` to run the api and execute it on port 8000

# Objective
* Understand the importance of mocking with an example that can only be tested by using mocks
* See different strategies for mocking
* Use mocking with dates and implement an exercise (how many seconds does the year have left?)
* Understand that web applications usually have databases, and you can not use the production database for testing with an example