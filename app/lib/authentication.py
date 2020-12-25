from app.lib.config import configuration


async def get_client(token):
    """
    Check if a client is authorized
    Returns the client_id for this request using the request headers
    """

    return configuration.authentication['tokens'][token]