from typing import Any, Dict


def handle_request(data: Dict[str, Any]) -> str:
    """Process incoming request data and return response.

    Args:
        data (Dict[str, Any]): The input data for processing.

    Returns:
        str: The response message after processing.
    """
    if not isinstance(data, dict):
        raise ValueError('Data must be a dictionary')

    # Simulate processing
    response = f"Processed data: {data}"
    return response


def log_response(response: str) -> None:
    """Log the response to the console.

    Args:
        response (str): The response message to log.
    """
    print(f'Response: {response}')