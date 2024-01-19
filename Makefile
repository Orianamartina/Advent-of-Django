install:
	poetry install
runserver:
	poetry run python manage.py runserver
runserverplus:
	poetry run python manage.py runserver_plus --nopin

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

shell:
	python manage.py shell