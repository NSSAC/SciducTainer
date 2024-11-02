FROM ghcr.io/nssac/mambascif

ARG VERSION
ENV VERSION=${VERSION:-0.0.0}

RUN mkdir -p /run/secrets

COPY config.json /
COPY src /src/
COPY apps.scif /
COPY environment.yml /

RUN --mount=type=secret,id=gh_token \
    curl --remote-name https://$(cat /run/secrets/gh_token)@raw.githubusercontent.com/NSSAC/SciducTainer/refs/heads/main/sciduct.scif \
    scif install /sciduct.scif && rm -f /sciduct.scif

RUN --mount=type=secret,id=gh_token \
    scif install /apps.scif && rm -f /apps.scif

RUN rm -rf /run/secrets || true

ENTRYPOINT ["scif"]

CMD ["shell"]