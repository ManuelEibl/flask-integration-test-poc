from typing import Generator

import pytest
from flask import Flask

from app.create_app import create_app


@pytest.fixture(scope="function")
def test_app() -> Generator[Flask, None, None]:
    app = create_app("testing")
    yield app
