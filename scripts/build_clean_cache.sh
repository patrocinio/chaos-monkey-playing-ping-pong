export IMAGE=ping_pong_clean_cache:latest
export IMAGE_PATH=patrocinio/$IMAGE

cd clean_cache

cp -r ../common .

docker build -t $IMAGE_PATH .
# docker login 
docker push $IMAGE_PATH

rm -rf common