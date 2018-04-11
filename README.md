# cernet-hawk

[![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/)

A port scan project.

# Installation

### Requirements

* nmap
* zmap
* rabbitmq

### Installation on Ubuntu

```shell
git clone https://github.com/sea0breeze/cernet-hawk.git
chmod +x cli/install.sh
chmod +x cli/iptables.sh
chmod +x do.sh

./cli/iptables.sh
./cli/install.sh
```

# Usage

## Config

Edit ``./config/cernet.conf``, pre-subnet pre-line
Edit ``./config/cernetv6.conf``, pre-IP pre-line

## Run

You can simply start this scanner after edit config file by:

```shell
./do.sh startall
```

After run, you can access ``127.0.0.1:5555`` to monitor this system
