# Docker File for General Stuff

FROM mcr.microsoft.com/vscode/devcontainers/universal:2-focal

RUN apt-get update && apt-get -y install --no-install-recommends \
    3.10.14-venv \
   gcc 

RUN apt install pandoc
   
ARG USER="codespace"
ARG VENV_PATH="/home/${USER}/venv"
COPY requirements.txt /tmp/
COPY Makefile /tmp/
RUN su $USER -c "/usr/bin/python3 -m venv /home/${USER}/venv" \
   && su $USER -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt" \
   && rm -rf /tmp/requirements.txt 