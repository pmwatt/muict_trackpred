# trackpred backend
files used
- `main.py`
  - responsible for running fastapi prediction web service.
- `model.py`
  - used to create and store our ML model in the first place. For docker, this doesn't need to be run, but we've included it as a reference of how we made the model in the first place.

# building and running docker image
1. if not done already, navigate to this folder in your shell(`trackpred_api`)
2. run `docker build -t trackpred/backend .` to build the frontend image
3. run `docker run -p 80:80 --name <your_container_name> trackpred/backend` to create and run the container based on the created image
   1. This is a bad practice because we hard-coded port 80, which means that if anyone wants to change the port number, you need to also change `PORT` in `/trackpred_flask/main.py` too.
4. Now run the frontend flask webserver