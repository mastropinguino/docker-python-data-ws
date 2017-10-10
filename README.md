# Docker Python Data Webservices
A base docker image for building python webservices that perform data analysis.

## Contents of image
The image is based on official python:3.6-slim image, with the following additions:

* [numpy >=1.12](http://www.numpy.org/)
* [pandas >=0.19](http://pandas.pydata.org/)
* [netCDF4 >=1.2.9](http://unidata.github.io/netcdf4-python/)
* [h5py >=2.7.1](http://www.h5py.org/)
* [Flask >=0.12](http://flask.pocoo.org/)
* [gunicorn >=19.7.1](http://gunicorn.org/)

## Usage
This image should not be used as a standalone container, but rather as a base image for your own applications/containers.
The image is bundled with an example flask application stored in /srv/app/ directory.
The application is booted by gunicorn HTTP server, with configuration stored at /srv/gunicorn_cfg.py.

To use image, simply base your _Dockerfile_ on it with:

```Dockerfile
FROM mastropinguino/python-data-ws:3.6
```

copy the application into _/srv/app/_ folder:

```Dockerfile
COPY . /srv/app/
```

and launch _pip install_ if more packages are needed:

```Dockerfile
RUN cd /srv/app/ && pip install -r requirements.txt
```

Build and run the container

```bash
$ docker build -t awesome-app-image:latest .

$ docker run -d -p 80:8000 awesome-app-image:latest
```

A complete skeleton of app could be found in [example](./example/helloworld) folder

## Contributions

Contributions are always welcome!
Feel free to let me know your thoughts or improvements.
