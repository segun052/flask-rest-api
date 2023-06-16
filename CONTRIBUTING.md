# CONTRIBUTING

## How to run the dockeer file locally

```
code
docker build -t flask-smorest-api .
docker run -dp 5000:5000 -w / app -v "$(pwd):/app IMAGE_NAME sh -c flask run --host 0.0.0.0"

comment
IMAGE_NAME is the name of the image you want to build on docker, the project name e.g. flask-smorest-api
```