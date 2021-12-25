# Github status 

## Build the image

`docker build . -t githubstatus:1.0`

## Run the container

`docker run -d githubstatus:1.0 --name githubstatus`

## Watch stdout:

`docker logs githubstatus`