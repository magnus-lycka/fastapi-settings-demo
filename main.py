from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Settings Demo. Default in Python code."
    admin_email: str
    admin_password: str
    something_else: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="demo_",
        secrets_dir='./secrets',
    )


settings = Settings()
app = FastAPI()


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "admin_password": settings.admin_password,
        "something_else": settings.something_else,
    }