create_env:
	cp ./config/docker/env ./config/docker/.env

up:
	docker-compose up -d