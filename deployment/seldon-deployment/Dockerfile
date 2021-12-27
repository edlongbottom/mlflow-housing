FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Port for GRPC
EXPOSE 5000
# Port for REST
EXPOSE 9000

# Define environment variable
ENV MODEL_NAME MyModel
ENV SERVICE_TYPE MODEL

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE