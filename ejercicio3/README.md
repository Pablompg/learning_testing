# Exercise 3. Testing simple apis without database.

In this exercise we are going to have a very simple api with only one endpoint.
Our aim is to test it end to end.

The api is built with fastapi and uvicorn. For testing we use pytest.

# Requirements
* Have python 3.11 or higher installed
* Have poetry installed

# Instructions
* `poetry install` to install dependencies
* `poetry run pytest` to execute the test suite
* `poetry run uvicorn main:app --reload` to run the api and execute it on port 8000

# Objective
* See a very simple API with fastapi and write a test for it
* Understand that when you choose a framework, you will need to learn how to test the framework. Vendor locked-in concept