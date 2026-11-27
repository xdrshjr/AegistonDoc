import pytest
from kb_workers.celery_app import create_celery_app


def test_celery_defaults_on_windows(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CELERY_BROKER_URL", raising=False)
    monkeypatch.delenv("CELERY_RESULT_BACKEND", raising=False)

    with create_celery_app(platform="win32") as app:
        assert app.conf.broker_url == "redis://127.0.0.1:6379/1"
        assert app.conf.result_backend == "redis://127.0.0.1:6379/2"
        assert app.conf.worker_pool == "solo"


def test_celery_env_config_and_default_pool_on_linux(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("CELERY_BROKER_URL", "redis://localhost:6380/3")
    monkeypatch.setenv("CELERY_RESULT_BACKEND", "redis://localhost:6380/4")

    with create_celery_app(platform="linux") as app:
        assert app.conf.broker_url == "redis://localhost:6380/3"
        assert app.conf.result_backend == "redis://localhost:6380/4"
        assert app.conf.worker_pool == "prefork"
