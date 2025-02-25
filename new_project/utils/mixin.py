from logging import Logger

from new_project.utils.root_logging import root_logger


class LoggingMixin:
    """A mixin class to add logging interface.

    Example:
        class MyClass(LoggingMixin, AnotherParentClass):
            def my_method(self) -> None:
                self.logger.debug("debug message")
    """

    @property
    def logger(self) -> Logger:
        """Return the logger of the class."""
        return root_logger.getChild(self.__class__.__qualname__)
