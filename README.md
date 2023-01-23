# Project Title: Podcast Episode Kafka Delivery System 


### Description:
This project is designed to deliver podcast episodes to users via a web API built with FastAPI and streaming them through Apache Kafka. The podcast episodes are stored in a Parquet file format and are processed using the Pandas library.

The system is composed of two main parts:

* The API server: A web server built using FastAPI that exposes an endpoint for users to request podcast episodes. The server queries the parquet file for the requested episode and streams it through Kafka to the user.
* The Kafka cluster: A cluster of Apache Kafka brokers that handle the streaming of the podcast episodes from the API server to the users.

The project makes use of the following technologies:

* FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
* Apache Kafka: A distributed streaming platform that is used to handle the streaming of the podcast episodes.
* Pandas: A library for working with various data.
* Parquet: columnar storage format of Hadoop ecosystem, which provides efficient storage and encoding of data.
* Docker Compose: A tool for defining and running multi-container Docker applications.

Getting started:
1. Clone the repository to your local machine.
2. Make sure you have Docker and Docker-compose installed.
3. Build the images by running docker-compose build
4. Start the containers using docker-compose up
5. Test the API endpoints using a tool like Postman or curl.

Endpoints:
* `GET /podcast/episode_id/{_id}` : Retrieve a specific episode by providing the episode_id in the url
* `GET /podcast/episode_find/{title}` : Retrieve a specific episode by providing the title name
* `GET /podcast/show_id/{_id}` :  Retrieve a specific show by providing the show_id in the url
* `GET /podcast/show_find/{title}` : Retrieve a specific show by providing the title name

**Note** : You need to have a parquet file containing the podcast episodes, if you don't have one you can create one using the provided functions in utils.py or any other way you prefer.
Also, you can find the `docker-compose.yml` file in the root of the project, which defines the services, networks, and volumes for the application.

Please let me know if you need more help or if you have any questions.