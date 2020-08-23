# Download base image ubuntu:latest
FROM ubuntu:latest

# Information about custom image
LABEL maintainer="prkprime007@gmail.com"

# install packages via script
COPY install-packages.sh .
RUN chmod +x install-packages.sh
RUN ./install-packages.sh

# copy files to container
COPY . /blog
WORKDIR /blog

# install pythonrequirements
RUN pip3 install --no-cache-dir -r requirements.txt

# expose the port 8080
EXPOSE 8000

CMD ["gunicorn", "-b 0.0.0.0:8000", "app:app"]