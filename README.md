# godot_assignment
Assignment Project by Go Dot

## Downloading and running

```bash
# Clone the project repository
$ git clone https://github.com/vin-ai/godot_assignment.git
# CD to project directory
$ cd godot_assignment
# Create Python3 based Virtual Environment
$ python3 -m venv pyenv
# Activate the new environment
$ source pyenv/bin/activate
# Install the project deps
$ pip install -r requirements.txt
# Ask Django to create migrations if any
$ python manage.py makemigrations
# Migrate the pending/new migrations
$ python manage.py migrate
# Publish the static contents to serve by webserver like Nginx/Apache
$ python manage.py collectstatic
# Run Django server fortesting purpose, else Gunicorn and Nginx will handle this
$ python manage.py runserver
```
