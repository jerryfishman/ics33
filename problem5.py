import contextlib

class OutIndexError(Exception):
    pass

class OutValueError(Exception):
    pass


@contextlib.contextmanager
def should_raise(type_error):
    pass

with should_raise(ValueError):
    int("Boo")