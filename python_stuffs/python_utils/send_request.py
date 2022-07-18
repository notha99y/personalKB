import json
import textwrap

import requests


def print_request_response(response):
    """
    # Read: https://stackoverflow.com/a/61803546
    """

    def headers(raw_headers):
        return "\n".join(f"{k}: {v}" for k, v in raw_headers.items())

    print(
        textwrap.dedent(
            """
        ================ [Request] ================

        {request.method} {request.url}
        {request_headers}

        {request_body}

        ================ [Response] ================

        {response.status_code} {response.reason} {response.url}
        {response_headers}

        {response.text}

        ============================================
            """
        ).format(
            request=response.request,
            response=response,
            request_body=(response.request.body or ""),  # .decode(),
            request_headers=headers(response.request.headers),
            response_headers=headers(response.headers),
        )
    )


def send_request(http_host: str, http_method: str, http_path: str, data: dict):
    """"
    Args:
        http_host (str): google.com
        http_method (str): POST
        http_path (str): /cool
        data (dict): request fields

    Returns:
        response
    """

    http_url = "http://" + http_host + http_path
    print(http_url)

    http_body = json.dumps(data)
    content_type = "application/json;charset=utf-8"

    request = requests.Request(
        method=http_method,
        url=http_url,
        data=http_body,
        headers={"Content-Type": content_type,},
    ).prepare()

    response = requests.Session().send(request)

    return response
