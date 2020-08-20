# NginxDockerProxy

[![Build Status](https://travis-ci.com/hansehe/NginxDockerProxy.svg?branch=master)](https://travis-ci.com/hansehe/NginxDockerProxy)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

[NginxDockerProxy](https://github.com/hansehe/NginxDockerProxy) is a simple tool to embed environment variables with nginx.

The latest Dockerfile is marked as: `hansehe/nginx-docker-proxy:latest`
- https://hub.docker.com/repository/docker/hansehe/nginx-docker-proxy

Please have a look at [example/nginx.site.conf](./example/nginx.site.conf) with this [example/Dockerfile](example/Dockerfile) example.

Any keys marked with `${key}` in a nginx site.conf file will be replaced with matching environment variable keys.

## Prerequisites
- Install [DockerBuildManagement](https://github.com/DIPSAS/DockerBuildManagement) buildsystem:
    - pip install DockerBuildManagement
- Install Dependencies:
    - pip install -r src/requirements.txt
- Note! Working directory should be `src/NginxDockerProxy/` when developing with pycharm etc or running tests or the `main.py`.

## Run Unit Tests Manually
- cd src/NginxDockerProxy
- python -m unittest

## Build, Test & Publish With DockerBuildManagement
- Build & Test:
    - `dbm -build -test`
- Run:
    - `dbm -run`
- Publish:
    - `dbm -publish`