# MyAPI

## Quickstart

```bash
# In activated venv, install dependencies
pip install --upgrade --constraint=requirements.txt --editable='.[dev]'
```

```bash
# Run FastAPI app
uvicorn myapi.main:app --reload
```

## Deploy to AWS Lambda

```bash
aws configure
aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <ECR>.amazonaws.com
docker build --platform=linux/amd64 -t myapi .
docker tag myapi:latest <ECR>.amazonaws.com/myapi:latest
docker push <ECR>.amazonaws.com/myapi:latest
```

## Additional info

- Excellent FastAPI + HTMX tutorial: https://www.youtube.com/watch?v=yu0TbJ2BQso
