FROM python:3.8.12-slim

# update local package indexes + packages and update pip
RUN apt update && apt upgrade -y && /usr/local/bin/python -m pip install --upgrade pip
# add a mqtt user so we don't need root
RUN groupadd -r mqtt && useradd -r -m -g mqtt mqtt
# use a separate directory for our application
WORKDIR /app
# let the running user own the app
COPY --chown=mqtt:mqtt requirements.txt /app/
COPY --chown=mqtt:mqtt main.py /app/
# switch to the user which will run the app
USER mqtt
# install paho-mqtt
RUN pip3 install -r requirements.txt
# run the script
ENTRYPOINT [ "python3", "./main.py" ]