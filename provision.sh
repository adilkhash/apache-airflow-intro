#!/usr/bin/env bash

bootstrap() {
  sudo apt-get update
  sudo apt-get upgrade
  echo "Installing system libs..."
  echo ""
  sudo apt-get -y install build-essential
  sudo apt-get -y install python3-dev
  sudo apt-get -y install python3-venv
  sudo apt-get -y install libxml2-dev libxslt1-dev
  sudo apt-get -y install lib32z1-dev
  sudo apt-get -y install libtiff5-dev
  sudo apt-get -y install libffi-dev
  sudo apt-get -y install libfreetype6-dev
  sudo apt-get -y install libpq-dev
  sudo apt-get -y install libssl-dev
  sudo apt-get -y install swig
  sudo apt-get -y install git
  sudo apt-get -y install gettext
  sudo apt-get -y install python3-pip
}

export DEBIAN_FRONTEND=noninteractive

bootstrap
