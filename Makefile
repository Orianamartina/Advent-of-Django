run-server:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

make-migrations:
	poetry run python manage.py makemigrations