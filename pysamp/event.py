import functools

from .callbacks import registry


def event(callback_name):
    def named_event(args_converter):
        @functools.wraps(args_converter)
        def register(cls, handler):
            @functools.wraps(handler)
            def wrapper(*args):
                return handler(*args_converter(cls, *args))

            registry.register_callback(
                callback_name,
                wrapper,
                args_converter.__name__,
            )
            return handler

        return classmethod(register)

    return named_event
