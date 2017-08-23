export IMAGE=ping_pong_throw_ball:latest
export ICP_DTR=9.19.34.109:8500
export IMAGE_PATH=$ICP_DTR/ping-pong/$IMAGE

docker build -t $IMAGE_PATH .
docker login $ICP_DTR
docker push $IMAGE_PATH
