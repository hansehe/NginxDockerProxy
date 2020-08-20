# NginxDockerProxy - Example
A simple example on how to use NginxDockerProxy with a website.
The NginxDockerProxy enables easy configuration with environment variables in nginx config files.

Please have a look at [nginx.site.conf](./nginx.site.conf) with this [Dockerfile](Dockerfile).

Any keys marked with `${key}` in a nginx site.conf file will be replaced with matching environment variable keys.

## Prerequisites
- Install [DockerBuildManagement](https://github.com/DIPSAS/DockerBuildManagement) buildsystem:
    - pip install DockerBuildManagement

## Build & Publish With DockerBuildManagement
- Build & Run:
    - `dbm -start -build -run -stop`
    - Access rabbitmq dashboard (username/password = amqp/amqp) at:
        - http://localhost:8080/
    - Check status health at:
        - http://localhost:8080/status/health
- Publish:
    - `dbm -publish`