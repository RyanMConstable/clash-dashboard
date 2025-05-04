FROM postgres:17.4

ENV POSTGRES_PASSWORD=changeme
ENV POSTGRES_DB=cocdb

COPY 01-init.sql /docker-entrypoint-initdb.d/
