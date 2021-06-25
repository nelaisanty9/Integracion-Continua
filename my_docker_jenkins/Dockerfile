FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt-get update && apt-get install -y nano
USER jenkins
RUN echo -e "jenkins ALL=(ALL) NOPASSWD:ALL" /etc/sudoers
