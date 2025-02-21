# fastapi-settings-demo
Demonstrate FastAPI settings/config with pydantic-settings

See https://docs.pydantic.dev/latest/concepts/pydantic_settings/

## Running it

    python3 -m venv .venv
    source . ./.venv/bin/activate
    pip install -e .
    export demo_admin_password=email-in-environment
    cp default.env .env
    fastapi dev main.py

Browse to http://127.0.0.1:8000/docs and try it out.

