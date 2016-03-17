FROM andrewosh/binder-base

MAINTAINER Sam Lau <samlau95@gmail.com>

USER root

RUN pip3 install --ignore-installed datascience

USER main

