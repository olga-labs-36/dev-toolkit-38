from typing import List, Dict, Any


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary.

    Args:
        nested_dict (Dict[str, Any]): The nested dictionary to flatten.
        parent_key (str, optional): The base key string. Defaults to ''.
        sep (str, optional): Separator for flattened keys. Defaults to '_'.

    Returns:
        Dict[str, Any]: A flattened dictionary.
    """  
    items = []
    for key, value in nested_dict.items():
        new_key = f'{parent_key}{sep}{key}' if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks.

    Args:
        items (List[Any]): The list to split.
        chunk_size (int): The size of each chunk.

    Returns:
        List[List[Any]]: A list of chunks.
    """  
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries.

    Args:
        dict1 (Dict[str, Any]): The first dictionary.
        dict2 (Dict[str, Any]): The second dictionary.

    Returns:
        Dict[str, Any]: A dictionary containing merged contents.
    """  
    merged = dict1.copy()
    merged.update(dict2)
    return merged
