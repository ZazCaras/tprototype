
FROM docker.io/python:3.10-slim-bullseye
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN ln -s /usr/local/bin/python3 /usr/bin/python3
RUN useradd -ms /bin/sh -u 1000 docker
USER docker
WORKDIR /app
VOLUME /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app.py /app/
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]