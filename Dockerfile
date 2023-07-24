FROM nvidia/cuda:11.8.0-devel-ubuntu20.04 as base

WORKDIR /workspace

COPY . .

ENV HUGGINGFACE_HUB_CACHE=/data

# install python3
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# install fastchat
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install . \
    && rm -rf /root/.cache/pip

ENTRYPOINT ["python3", "entrypoint.py"]
CMD ["--help"]
