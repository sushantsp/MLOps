### Docker Image LifeCycle

1. Creation : Build a new image from the dockerfile or pull one from the registry

2. Storages : Images are stored locally in your docker env and can be pushed to remote registries for production pull and use.

3. Distribution : Images can be shared or distributed by pushing them to a public or private repo. 

4. Execution : Running instance of the image is called container. You need to run the image like starting a server or a machine. 



1. Build a docker Image : `docker build -t mlops_docker`
2. Run the container : `docker run -p 5000:5000 mlops_docker`
3. Tag the image for Hub : `docker tag mlops_docker <username>/mlops_docker:latest`
4. Push the image to the hub : `docker push <username>/mlops_docker:latest`
5. Pull the Images : `docker pull <username>/mlops_docker:latest`