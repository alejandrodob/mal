FROM ubuntu:vivid
MAINTAINER Joel Martin <github@martintribe.org>

##########################################################
# General requirements for testing or common across many
# implementations
##########################################################

RUN apt-get -y update

# Required for running tests
RUN apt-get -y install make python

# Some typical implementation and test requirements
RUN apt-get -y install curl libreadline-dev libedit-dev

RUN mkdir -p /mal
WORKDIR /mal

##########################################################
# Specific implementation requirements
##########################################################

# Julia
RUN apt-get -y install software-properties-common
RUN apt-add-repository -y ppa:staticfloat/juliareleases
RUN apt-get -y update
RUN apt-get -y install julia

