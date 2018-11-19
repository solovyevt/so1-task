# Spring Boot on Docker connecting to MySQL Docker container

1. Use MySQL Image published by Docker Hub (https://hub.docker.com/_/mysql/)
Command to run the mysql container
`docker run --name mysql-standalone -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=test -e MYSQL_USER=sa -e MYSQL_PASSWORD=password -d mysql:5.6`

2. In the Spring Boot Application, use the same container name of the mysql instance in the application.properties
`spring.datasource.url = jdbc:mysql://mysql-standalone:3306/test`

3. Create a `Dockerfile` for creating a docker image from the Spring Boot Application
`FROM openjdk:8
ADD target/users-mysql.jar users-mysql.jar
EXPOSE 8086
ENTRYPOINT ["java", "-jar", "users-mysql.jar"]`

4. Using the Dockerfile create the Docker image.
From the directory of Dockerfile - `docker build . -t users-mysql`

5. Run the Docker image (users-mysql) created in #4.
`docker build . -t users-mysql`

## Useful Docker commands
- `docker images`
- `docker container ls`
- `docker logs <container_name>`
- `docker container rm <container_name`
- `docker image rm <image_name`


## Kubernetes
This project requires Helm for Kubernetes deployment. Suit helm/values.yaml for your needs and then 
call.

To deploy this image to Kubernetes cluster you must do the following steps:

####1. Build Docker image from sources and push it to the public registry accessible to the Kubernetes cluster

`docker build -t registry.gitlab.com/zukokolkka/docker-mysql-spring-boot-example:test .`

`docker push registry.gitlab.com/zukokolkka/docker-mysql-spring-boot-example:test `

####2. Deploy using Helm

2.1 `helm init` first to deploy Tiller to Kubernetes cluster

2.2 `helm dependencies build` to pull MySQL Helm Chart as a dependency

2.3 Edit helm/values.yaml depending on your environment

2.4 Untar charts/mysql.tgz and edit helm/charts/mysql/values.yaml, don't forget to enable persistence.

After creation, mysql deployment creates PVC, so you need to create PersistentVolume manually or use VolumeProvisioner.

2.5 Finally, deploy this demo project 

``helm install helm/ -f helm/values.yaml -n test-spring-boot --namespace test``


## Jenkins

Jenkinsfile is located in root folder, it implements the most basic CI pipeline using Kubernetes + Helm

1. **Build develop images from develop branch**
2. **Run develop tests**
3. **Deploy develop environment**
4. **Build staging images from master branch**
5. **Run staging tests**
6. **Deploy staging environment**
7. **Build production images from master branch** 
8. **Run production tests**
9. **Deploy production environment** (Triggered manually)






 

