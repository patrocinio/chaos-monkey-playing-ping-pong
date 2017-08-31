export IMAGE=ping_pong_commentator:latest
export IMAGE_PATH=patrocinio/$IMAGE

cp -r ../common .

docker build -t $IMAGE_PATH .
# docker login 
docker push $IMAGE_PATH

rm -rf common