def singleton(cls):
    """Singleton Decorator."""
    instances = {}

    def wrapper(*args, **kwargs):
        """A wrapper for Singleton instances."""
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
