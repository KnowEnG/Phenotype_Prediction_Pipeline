# Building The Data Cleanup Pipeline Docker Image
The Dockefile in this directory contains all the commands, in order, needed to build the **Phenotype Prediction Pipeline** docker image.


* Run the "make" command to build the **Data Cleanup Pipeline** docker image (output: docker image called "phenotype_prediction_pipeline" and a tag with today's date and time):
```
    make build_docker_image
```

* Login to docker hub. When prompted, enter your password and press enter:
```
    make login_to_dockerhub username=(enter your docker login here) email=(enter your email here)
```

* Upload your image to docker hub:
```
    make push_to_dockerhub
```

* * * 
## How to run this docker image
* * * 

1 Change directory to the directory  where you want to run.

2 docker run -v \`pwd\`:/home/test/run_dir/ -it knowengdev/phenotype_prediction_pipeline:01_06_2017 

3 cd test

4 make env_setup

5 edit the .yml file (use the comments to see options)

* Check on docker.hub to get the latest image. 

* If you don't "cp" your data into the volume you mounted it will disappear when you exit docker.
