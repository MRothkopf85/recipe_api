FROM debian:stretch-slim

RUN apt-get update && \
    apt-get install -y python3 \
    python3-pip \
    curl

RUN useradd -m recipe && \
    mkdir -p /opt/recipe_api && \
    chown recipe:recipe /opt/recipe_api

WORKDIR /opt/recipe_api

COPY . .

RUN pip3 install -r requirements.txt

USER recipe

CMD ["python3", "app.py"]
