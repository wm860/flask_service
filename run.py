from waitress import serve
from app_flask import app

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8001)