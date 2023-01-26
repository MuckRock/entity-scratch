db:
	docker compose --env-file .env up

run:
	python manage.py runserver
