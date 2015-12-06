# A standalone Docker image

There are two ways to use this Docker image. You can either build your own image from `Dockerfile` or `docker pull` from Dockerhub.

## Build your own

To build to own image, clone the repository

```shell
git clone https://github.com/UI-DataScience/info490-fa15
```

or if you have already cloned it, change into `info490-fa15/docker-standalone` directory

```shell
cd info490-fa15/docker-standalone
```

Build a Docker image with

```shell
docker build --rm -t lcdm/standalone-info490 .
```

## Docker pull

Pull the image from Dockerhub by doing

```shell
docker pull lcdm/standalone-info490
```

## Run IPython/Jupyter notebook server

To run an Ipython/Jupyter notebook server, run

```shell
docker run -d -p 8888:8888 --name standalone lcdm/standalone-info490
```

Open your web browser, and now you can access the notebook server at `127.0.0.1:8888` or `localhost:8888`.
