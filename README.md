# fastapi-settings-demo
Demonstrate FastAPI settings/config with pydantic-settings

See https://docs.pydantic.dev/latest/concepts/pydantic_settings/

## Running it

    python3 -m venv .venv
    source . ./.venv/bin/activate
    pip install -e .
    export demo_admin_password=email-in-environment
    fastapi dev main.py

Browse to http://127.0.0.1:8000/docs and try it out.

Expected response from GET http://127.0.0.1:8000/info

    {
      "app_name": "Settings Demo. Default in Python code.",
      "admin_email": "email-in-environment",
      "admin_password": "secret_in_secrets_file",
      "something_else": "something else in env file"
    }
