# MLOps with MLFlow and Seldon Core

This project demonstrates the use of open-source toolkits MLFlow and Seldon Core to aid in the deployment and operation of Machine Learning (ML) models. The Boston Housing dataset from sklearn is used as a simple use case to show the tools in action and demonstrate the workflow.

MLFlow provides tools for tracking experiments, logging parameters and scores, storing models and packaging code during the Experimentation phase. It also allows deployment of models with an MLFlow model server so they can be served as a prediction web service. 

Using Seldon Core introduces a number of benefits:
 - Pre-built reusable model servers available as docker images with associated K8s CRDs / Helm Charts
 - Model servers available for models packaged using sklearn or mlflow
 - Automated ingress configuration
 - Integration with monitoring/tracing and analytics solutions

This repo is in two sections: Experimentation and Deployment.

## Experimentation

This phase includes Exploratory Data Analysis (EDA), feature engineering, and model building, training and evaluation. Notebooks are available in this folder each for EDA and model building with MLFlow, which is currently configured to create a local SQLite database for storing experiment data and save model artefacts locally under the Experimentation folder.   

### Deployment

This folder includes a notebook and scripts for the deployment of a ML model or pipeline using a variety of approaches:
1. Deploying on a local MLFlow REST server
2. Deploying as a containerised service locally on Docker Desktop
3. Deploying to a remote Kubernetes instance using Seldon Core

While an attempt has been made to design the scripts to be transferrable as possible for use in other projects without the need for any additional code, the python class wrapper (MyModel.py) would need to be amended depending on the model/pipeline and the input format it expects. This is intended as a set of scripts for streamline the deployment of ML models to Kubernetes as robust and scalable prediction web services.