create_env:
	cp ./config/docker/env ./config/docker/.env

up:
	docker compose up --build

force_up:
	docker compose up --force-recreate

env_load:
	config/docker/env_load.sh config/docker/.env
