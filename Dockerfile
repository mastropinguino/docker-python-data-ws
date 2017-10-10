FROM python:3.6-slim
LABEL maintainer="mastropinguino@networky.net"

COPY app.py /srv/app/
COPY gunicorn_cfg.py /srv/

# Install the required packages & remove pip cache to reduce size
RUN cd /srv/app && \
    pip install \
        "numpy>=1.12" \
        "pandas>=0.19" \
        "netCDF4>=1.2.9" \
        "h5py>=2.7.1" \
        "Flask>=0.12" \
        "gunicorn>=19.7.1" && \
    rm -rf /root/.cache

# PYTHONUNBUFFERED: Force stdin, stdout and stderr to be totally unbuffered. (equivalent to `python -u`)
# PYTHONHASHSEED: Enable hash randomization (equivalent to `python -R`)
# PYTHONDONTWRITEBYTECODE: Do not write byte files to disk, since we maintain it as readonly. (equivalent to `python -B`)
ENV PYTHONUNBUFFERED=1 PYTHONHASHSEED=random PYTHONDONTWRITEBYTECODE=1

# Default port
EXPOSE 8000

WORKDIR /srv/app
CMD [ "gunicorn", "-c", "/srv/gunicorn_cfg.py", "app:app" ]
