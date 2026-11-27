import os
import sys

from celery import Celery


def create_celery_app(*, platform: str | None = None) -> Celery:
    app = Celery(
        "kb_workers",
        broker=os.getenv("CELERY_BROKER_URL", "redis://127.0.0.1:6379/1"),
        backend=os.getenv("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/2"),
    )
    if (sys.platform if platform is None else platform) == "win32":
        app.conf.worker_pool = "solo"
    return app


celery_app = create_celery_app()
