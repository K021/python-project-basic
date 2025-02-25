from typing import Any, ClassVar, Dict

Class = Any
Instance = Any


class Singleton(type):
    """A metaclass to make a class a singleton."""

    _instances: ClassVar[Dict[Class, Instance]] = {}

    def __call__(cls, *args, **kwargs) -> Any:
        """Returns the instance of the class.

        Initializes the instance of the class if it has not been initialized before.
        And seals the class to prevent reinitialization.

        Returns:
            Singleton: The instance of the class.
        """
        # Initialize the instance of the class if it has not been initialized before.
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            # Get the instance of the class.
            instance = cls._instances[cls]
            # Reinitialize it without creating a new instance, if allowed.
            if hasattr(cls, "__allow_reinitialization") and cls.__allow_reinitialization:
                instance.__init__(*args, **kwargs)  # call the init again
        return instance

    @classmethod
    def clear(_cls, cls: Any):
        """Clears the instance of the class."""
        _cls._instances.pop(cls, None)
