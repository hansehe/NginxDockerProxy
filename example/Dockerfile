FROM hansehe/nginx-docker-proxy:latest as dev

# Any module installation such as 'npm install' should be done here.

FROM dev as final

# Remove health check if /status/health url is removed.
HEALTHCHECK --interval=30s --timeout=10s --retries=3 --start-period=10s CMD curl --silent --fail localhost:80/status/health || exit 1

# All sites should be placed under /etc/nginx/conf.d/
WORKDIR /etc/nginx
COPY nginx.site.conf conf.d/nginx.site.conf