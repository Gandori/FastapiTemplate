sudo docker-compose down

docker rmi fastapi-template

sudo docker-compose -f docker-compose.dev.yml up --detach --build