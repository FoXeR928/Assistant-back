import uvicorn
from app import app
from config.config_init import ip, port


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=ip,
        port=port,
    )