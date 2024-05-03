# trackpred backend
files used
- `main.py`
  - responsible for running fastapi prediction web service.
- `model.py`
  - used to create and store our ML model in the first place. For docker, this doesn't need to be run, but we've included it as a reference of how we made the model in the first place.

# building and running docker image
1. if not done already, run `docker network create trackpred` **once**. this is because we have two containers interacting together, and we need to connect them via the `trackpred` network using their network aliases. see [here](https://docs.docker.com/get-started/07_multi_container/) for more reference details.
2. navigate to this folder in your shell (`trackpred_api`)
3. run `docker build -t trackpred/be .` to build the frontend image
4. run `docker run -p 80:80 --network trackpred --network-alias be trackpred/be` to create and run the container based on the created image
5. Now run the frontend flask docker container