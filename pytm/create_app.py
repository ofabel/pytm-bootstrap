from os import getcwd
from pathlib import Path
from typing import Optional
from typing import TYPE_CHECKING

from flask import Flask

from .api import API

if TYPE_CHECKING:
    from .abstract_exercise import AbstractExercise


def create_app(exercise: 'AbstractExercise', static_folder_path: Optional[str]) -> Flask:
    api: API = API(exercise)

    static_folder: str = static_folder_path if static_folder_path else Path(getcwd()).joinpath('static')

    app = Flask(import_name=__name__,
                static_folder=static_folder,
                static_url_path='/static')

    app.register_blueprint(api.blueprint, url_prefix='/api/v1')

    return app
