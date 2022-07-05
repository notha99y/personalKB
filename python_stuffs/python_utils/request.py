import textwrap

def print_request_response(response):
    """
    # Read: https://stackoverflow.com/a/61803546
    """
    def headers(raw_headers):
        return '\n'.join(f'{k}: {v}' for k, v in raw_headers.items())

    print(textwrap.dedent('''
        ================ [Request] ================

        {request.method} {request.url}
        {request_headers}

        {request_body}

        ================ [Response] ================

        {response.status_code} {response.reason} {response.url}
        {response_headers}

        {response.text}

        ============================================
            ''').format(
        request=response.request,
        response=response,
        request_body=(response.request.body or ''),#.decode(),
        request_headers=headers(response.request.headers),
        response_headers=headers(response.headers),
    ))