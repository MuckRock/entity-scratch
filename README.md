# entity-prototype

Standalone prototype for trying out some ideas.

## Installation

- Clone this repo.
- `apt install python3-dev libpq5 libpq-dev` (Sometimes, you have uninstall and reinstall libpq5 for libpq-dev to be able to install. These are dependencies that psycopg2 needs.)
- `python3.9 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- Create a .env file in the repo root that looks like this:

    # postgres
    POSTGRES_PASSWORD=<your pg password>
    POSTGRES_USER=<the pg username you want>
    POSTGRES_DB=entity-prototype

    # django
    SECRET_KEY=<the secret key you want to use>

## Run it

- `make db`

And in another terminal:

- `source venv/bin/activate`
- `make run`
