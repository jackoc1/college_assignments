# syntax=docker/dockerfile:1s
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /usr/sr/app
COPY . .
RUN pip3 install matplotlib
CMD ["mandelbrot.py"]
ENTRYPOINT ["python3"]
