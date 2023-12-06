
ARG BASE=nvidia/cuda:11.8.0-base-ubuntu22.04
FROM ${BASE} as base

FROM python:3.11.1-buster as final



RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends gcc g++ make espeak-ng libsndfile1-dev && rm -rf /var/lib/apt/lists/*
# python3 python3-dev python3-pip python3-venv python3-wheel 
RUN pip3 install llvmlite --ignore-installed

# Install Dependencies:
RUN pip3 install torch torchaudio --extra-index-url https://download.pytorch.org/whl/cu118
RUN rm -rf /root/.cache/pip

WORKDIR /root
COPY . /root

RUN pip3 install -r requirements.txt
RUN pip3 install -U TTS

RUN pip3 install runpod

CMD [ "python3", "-u",  "handler.py" ]

# EXPOSE 8080
# CMD ["flask","run","--host=0.0.0.0","--port=8080"]