FROM postgres:17.4

ARG PUID=1000
ARG PGID=1000

RUN groupmod -g ${PGID} postgres && usermod -u ${PUID} -g ${PGID} postgres && chown -R postgres:postgres /var/lib/postgresql /var/run/postgresql

ENV POSTGRES_PASSWORD=changeme
ENV POSTGRES_DB=cocdb
ENV POSTGRES_USER=postgres

USER postgres

COPY 01-init.sql /docker-entrypoint-initdb.d/
