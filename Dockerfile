FROM ghcr.io/nssac/mambascif

RUN mkdir -p /run/secrets

COPY config.json /
COPY src /src/
COPY sciduct.scif /
COPY apps.scif /

RUN --mount=type=secret,id=gh_token \
    scif install /sciduct.scif && rm -f /sciduct.scif

RUN --mount=type=secret,id=gh_token \
    scif install /apps.scif && rm -f /apps.scif

RUN rm -rf /run/secrets || true

ENTRYPOINT ["scif"]

CMD ["shell"]