from subprocess import check_output
import json

from constants import (
    API_HOST,
    CONTENT_TYPE_OPTION,
    COOKIES_PATH,
)
from .common import get_csrf_token


def curl(method, payload=None, endpoint="", use_x_csrf_token=False):
    """
    params:
        method: str, HTTP Request command, only allow "GET", "POST" currently.
        payload: Optional[dict], request payload.
        endpoint: Optional[str], api endpoint
    return:
        curl response body
    """
    method = method.strip().upper()
    if method not in {"POST", "GET"}:
        return None
    cmd = "curl {content_type} -k -s -L --cookie '{cookie_file}'  --cookie-jar '{cookie_file}' ".format(
        content_type=CONTENT_TYPE_OPTION,
        cookie_file=COOKIES_PATH,
    )
    if use_x_csrf_token:
        cmd += " -H 'X-CSRFToken: {x_csrf_token}' ".format(
            x_csrf_token=get_csrf_token()
        )
    if payload:
        cmd += " -d '{data}' ".format(data=json.dumps(payload))
    cmd += (" -X {method} \"{api_host}/{endpoint}\"").format(
        method=method,
        api_host=API_HOST,
        endpoint=endpoint,
    )
    result = check_output(cmd, shell=True)
    str(result.decode(encoding="utf8"))
    return result
