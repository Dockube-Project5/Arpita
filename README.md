# Arpita
Dockube

## STEPS REQUIRED FOR DEPLOYING THE IMAGE OF A FLASK APPLICATION ON KUBERNETES

### Building a Docker image of your flask application
```
docker build -t <folder-name> .
```
#### Checking if the image is created
```
docker images
```
#### Running the containerized image
```
docker run -dp <port-name>:<port-name> <image-name>. Check if the image is running on the localhost using http://localhost:<port-name>
```

### Pushing the image on Docker Hub
#### Login to Docker Hub
```
docker login
```
#### Tagging the image
```
docker tag <image-name> <dockerhub-username>/<repository-name>:<tag-name>
```
#### Pushing the image
```
docker push <dockerhub-username>/<repository-name>:<tag-name>
```
  
### Deploying the image on Kubernetes
#### Applying the deployment.yaml file
```
kubectl apply -f deployment.yaml
```
#### Checking deployments
```
kubectl get deployments
```
#### Running the deployed image
```
curl http://localhost:<port-name>
```
