import uvicorn

import app


def run_server():
    config = uvicorn.Config(app=app.starlette_app, host="localhost", port=3000)
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    run_server()
