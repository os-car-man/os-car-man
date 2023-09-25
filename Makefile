.PHONY: build bash docs

build:
	docker build -t os-car-man:latest .

DOCKER_ENTRY := docker run --rm -it -v $$PWD:/home/docs/project -p 7777:7777 os-car-man:latest


docs:
	$(DOCKER_ENTRY) mkdocs serve -a 0.0.0.0:7777

bash:
	docker run --rm -it -v $$PWD:/home/docs/project os-car-man:latest bash
