FROM python:3.10-alpine

# Install dependicies
COPY deployment/requirements.txt .

RUN python -m pip install --upgrade pip

RUN apt update && \
    apt install -y \
    curl \
    git \
    nano \
    gcc \
    musl-dev && \
    ln -s /lib/ld-musl-x86_64.so.1 /lib/libc.musl-x86_64.so.1

# Make a directory
WORKDIR /app/src

# Environment variables
ENV PATH=$PATH:/app/vendor/bin

ENV PYTHONPATH=$PYTHONPATH:/app/vendor/lib/python3.10/site-packages

ENV PYTHONUNBUFFERED=1

# Run application
ENTRYPOINT ["sleep", "infinity"]
