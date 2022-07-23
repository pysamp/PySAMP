import functools
import inspect

from .callbacks import registry


def event(callback_name):
    def named_event(args_converter):
        @functools.wraps(args_converter)
        def register(cls, handler):
            annotations = [
                handler.__annotations__.get(parameter)
                for parameter in inspect.signature(handler).parameters
            ]

            @functools.wraps(handler)
            def wrapper(*args):
                args = [
                    annotation(arg) if annotation and (
                        not isinstance(annotation, type)
                        or not isinstance(arg, annotation)
                    ) else arg
                    for arg, annotation in zip(
                        args_converter(cls, *args),
                        annotations
                    )
                ]
                return handler(*args)

            registry.register_callback(
                callback_name,
                wrapper,
                args_converter.__name__,
            )

        return classmethod(register)

    return named_event
