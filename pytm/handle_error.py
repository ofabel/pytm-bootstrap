from traceback import format_exception
from typing import List

from flask import Response

from .method_call_exception import MethodCallException


def handle_error(log_exception: callable, error: Exception) -> Response:
    error_to_handle: Exception = error.__cause__ if isinstance(error, MethodCallException) else error
    lines: List[str] = format_exception(type(error_to_handle), error_to_handle, error_to_handle.__traceback__)
    error_as_str: str = ''.join(lines)

    log_exception(error_to_handle)

    return Response(response=error_as_str, status=500, mimetype='text/plain')
