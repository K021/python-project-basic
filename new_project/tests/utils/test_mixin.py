import logging

from new_project.utils.mixin import LoggingMixin


def test_logging_mixin(caplog):
    """Test the LoggingMixin class."""
    caplog.set_level(logging.DEBUG)

    class A(LoggingMixin):
        def __init__(self):
            self.logger.debug("debug message")
            self.logger.info("info message")
            self.logger.warning("warning message")
            self.logger.error("error message")
            self.logger.critical("critical message")

    _ = A()

    # XXX: `new_project` needs to be changed to the actual project name.
    assert caplog.record_tuples == [
        ("new_project.test_logging_mixin.<locals>.A", 10, "debug message"),
        ("new_project.test_logging_mixin.<locals>.A", 20, "info message"),
        ("new_project.test_logging_mixin.<locals>.A", 30, "warning message"),
        ("new_project.test_logging_mixin.<locals>.A", 40, "error message"),
        ("new_project.test_logging_mixin.<locals>.A", 50, "critical message"),
    ]
