# trackpred frontend
files used
- `main.py`
  - this should be executed to start the flask webserver
- `request.py`
  - simply serves as a testing file for making request.

# building and running docker image
1. if not done already, navigate to this folder in your shell(`trackpred_flask`)
2. run `docker build -t trackpred/frontend .` to build the frontend image
3. run `docker run --name <your_container_name> trackpred/frontend` to create and run the container based on the created image
4. Navigate to the url running the flask webserver shown on the commandline similar to `http://0.0.0.0:5000`. This will run the frontend webserver for the form page UI. However, the backend fastapi prediction and result page part requires `trackpred/backend` container to run as well (see `trackpred_api` folder readme for more details).

# running without docker (for quick testing)
1. run `flask --apa main run --debug`