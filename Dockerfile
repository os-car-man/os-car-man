FROM python:3.11-slim-bullseye

RUN apt update && apt install -y git
COPY ci-requirements/entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh


ARG user=docs
RUN useradd --system --create-home $user


USER $user
RUN mkdir -p /home/$user/project
WORKDIR /home/$user/project

ENV PATH="$PATH:/home/$user/.local/bin"
COPY ci-requirements/requirements-3.11.out ci-requirements/requirements-3.11.out
RUN pip install -r ci-requirements/requirements-3.11.out

EXPOSE 7777

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
