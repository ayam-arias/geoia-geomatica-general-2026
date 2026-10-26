# Entorno reproducible del curso Geomática General · Chile 2026
FROM quay.io/jupyter/minimal-notebook:python-3.12

USER root
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
USER ${NB_UID}

COPY environment.yml /tmp/environment.yml
RUN mamba env update -n base -f /tmp/environment.yml && mamba clean -afy

WORKDIR /home/jovyan/trabajo
EXPOSE 8888
