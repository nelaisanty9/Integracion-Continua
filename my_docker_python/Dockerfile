FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN apt-get update && apt-get -y install vim && apt-get -y install bash
CMD ["/bin/bash"]
