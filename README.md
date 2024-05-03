# MUICT Track Prediction
![image](https://github.com/pmwatt/muict_trackpred/assets/87473156/b7c3a112-2210-410e-b101-efb9f482dd40)
![image](https://github.com/pmwatt/muict_trackpred/assets/87473156/17f069b4-dc0c-4e13-9c4d-7050483dc14d)

## Building and Running Frontend Flask
1. if not done already, run `docker network create trackpred` **once**. this is because we have two containers interacting together, and we need to connect them via the `trackpred` network using their network aliases. see [here](https://docs.docker.com/get-started/07_multi_container/) for more reference details.
2. navigate to this folder in your shell (`trackpred_flask`)
3. run `docker build -t trackpred/fe .` to build the frontend image
4. run `docker run -p 5000:5000 --network trackpred --network-alias fe trackpred/fe` to create and run the container based on the created image.
5. Navigate to the url running the flask webserver shown on the commandline. This will run the frontend webserver for the form page UI.
   1. However, the backend fastapi prediction and result page part requires `trackpred/backend` container to run as well (see `trackpred_api` folder readme for more details). So if not already, run the backend fastapi docker container.

## Building and Running Backend Fastapi
1. if not done already, run `docker network create trackpred` **once**. this is because we have two containers interacting together, and we need to connect them via the `trackpred` network using their network aliases. see [here](https://docs.docker.com/get-started/07_multi_container/) for more reference details.
2. navigate to this folder in your shell (`trackpred_api`)
3. run `docker build -t trackpred/be .` to build the backend image
4. run `docker run -p 80:80 --network trackpred --network-alias be trackpred/be` to create and run the container based on the created image
5. Now run the frontend flask docker container
