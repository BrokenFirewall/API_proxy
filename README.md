# API proxy assignment

This app uses dependencies that you have to manually install before launching it.


### Run application

- To run this application you have to use the command `flask run` from the `module` directory.
- To run test you can use `python -m test` from the `module` directory


- for debugging locally
- app.run(debug=True, host='0.0.0.0',port=5000)
- for production
- app.run(host='0.0.0.0', port=5000)

### Run Docker

- docker build -t demo/flask-api:0.0 .
- docker run --name demo-flask-api -d -p 3000:3000 demo/flask-api:0.0
