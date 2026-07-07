import os, sys
from app import app

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 9000))
    server = os.environ.get("WSGI_SERVER", "").lower()

    if server == "waitress":
        from waitress import serve
        print(f"[启动] Waitress -> http://{host}:{port}")
        serve(app, host=host, port=port)
    elif server == "gunicorn":
        from gunicorn.app.base import BaseApplication
        class GunicornApp(BaseApplication):
            def __init__(self, app, options):
                self.application = app
                self.options = options
                super().__init__()
            def load_config(self):
                for k, v in self.options.items():
                    self.cfg.set(k.lower(), v)
            def load(self):
                return self.application
        wcnt = 4
        opts = {"bind": f"{host}:{port}", "workers": wcnt, "accesslog": "-", "errorlog": "-"}
        print(f"[启动] Gunicorn -> http://{host}:{port} [{wcnt} workers]")
        GunicornApp(app, opts).run()
    else:
        print(f"[启动] Flask Dev -> http://{host}:{port}")
        app.run(host=host, port=port, debug=(os.environ.get("FLASK_DEBUG") == "1"))
