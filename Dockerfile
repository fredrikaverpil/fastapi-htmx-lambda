FROM public.ecr.aws/lambda/python:3.9

# Copy function code
COPY src .
COPY requirements.txt .
COPY pyproject.toml .
RUN pip install --upgrade --constraint=requirements.txt .
RUN pip install awslambdaric

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
#ENTRYPOINT [ "python", "-m", "myapi.main.handler"]
# CMD [ "myapi.main.handler" ]

ENTRYPOINT ["python", "-m", "awslambdaric"]
CMD [ "myapi.main.handler" ]
