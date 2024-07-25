# data-analytics-app

Project Overview

This project is a machine learning application that for the data analysis based on various features. It utilizes a dataset with historical house prices  The application is built using Python and leverages popular libraries such as  and pandas.
Table of Contents
    Setup Instructions
    How to Run Tests
    Deployment Instruction

Setup Instructions

To set up the project on your local machine, follow these steps:
Prerequisites

Ensure you have the following installed:

    Python 3.x
    pip (Python package installer)

Clone the Repository

git clone https://github.com/your-username/data-analysis-app.git
cd data-analysis-app

Create and Activate a Virtual Environment

bash

python -m venv venv
source venv/bin/activate  

Install Dependencies

bash

pip install -r requirements.txt

How to Run Tests

To ensure that your application works as expected, run the tests using:
pytest

Deployment Instructions

To deploy the application, follow these steps:
Docker Deployment

    Build the Docker image:

docker build -t data-analysis-app
Run the Docker container:

    docker run -p 5000:5000data-analysis-app
Kubernetes Deployment

    Apply the Kubernetes manifests:
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Verify deployment:

bash

kubectl get pods
kubectl get services
