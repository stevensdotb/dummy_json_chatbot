import json
import requests

from logger import logger
from settings import API_URL


def search_users(field:str, value:str, return_fields:list = []) -> dict:
    """Retrieves users from the internal database. Trigger only on Specific Identity queries.
    Args:
        field (str): User field to filter by, e.g. 'hair.color', 'age', 'gender'
        value (str): Value that the field must match
        return_fields (list, optional): List of user fields to return in the response.
    Returns:
        dict: The filtered user data or an error message.   
    """
    if return_fields and isinstance(return_fields, str):
        return_fields = json.loads(return_fields)

    q_params = f"key={field}&value={value}"
    q_search = f"&select={','.join(return_fields)}" if return_fields else ""

    query = f"filter?{q_params}{q_search}&limit=0"
    endpoint = f"{API_URL}/{query if field and value else ''}"
    logger.info(f"Endpoint: {endpoint}")

    response = requests.get(endpoint)
    if response.status_code >= 400:
        logger.error(response.text)
        return {"error": "Error fetching users"}

    return response.json()


def count_users() -> dict:
    """Counts the total number of users in the internal database.
    Returns:
        dict: The total user count or an error message.   
    """
    endpoint = f"{API_URL}"
    logger.info(f"Endpoint: {endpoint}")

    response = requests.get(endpoint)
    if response.status_code >= 400:
        logger.error(response.text)
        return {"error": "Error counting users"}

    data = response.json()

    if isinstance(data, dict) and data.get("total"):
        return {"total": data["total"]}
    
    return data


def get_user_posts(user_id: int) -> dict:
    """Retrieves posts made by a specific user on social medias.
    Args:
        user_id (int): The ID of the user whose posts are to be retrieved.
    Returns:
        dict: The user's posts or an error message.   
    """
    endpoint = f"{API_URL}/{user_id}/posts"
    logger.info(f"Endpoint: {endpoint}")

    response = requests.get(endpoint)
    if response.status_code >= 400:
        logger.error(response.text)
        return {"error": f"Error fetching posts for user {user_id}"}

    return response.json()


def get_user_todos(user_id: int) -> dict:
    """Retrieves to-do items assigned to a specific user.
    Args:
        user_id (int): The ID of the user whose to-do items are to be retrieved.
    Returns:
        dict: The user's to-do items or an error message.   
    """
    endpoint = f"{API_URL}/{user_id}/todos"
    logger.info(f"Endpoint: {endpoint}")

    response = requests.get(endpoint)
    if response.status_code >= 400:
        logger.error(response.text)
        return {"error": f"Error fetching todos for user {user_id}"}

    return response.json()


def call_function(name, args):
    if name == "search_users":
        return search_users(**args)
    elif name == "count_users":
        return count_users()
    elif name == "get_user_posts":
        return get_user_posts(**args)
    elif name == "get_user_todos":
        return get_user_todos(**args)
    else:
        return {"error": f"Function {name} not found."}


tools = [
    search_users,
    count_users,
    get_user_posts,
    get_user_todos
]