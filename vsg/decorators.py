# -*- coding: utf-8 -*-
import functools


def print_method_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        class_name = args[0].__class__.__name__ if args else "N/A"
        print(f"-->> {__name__}")
        print(f"Calling method: {class_name}.{func.__name__}")
        return func(*args, **kwargs)

    return wrapper


level = 0
display = True
display = False


def print_classifier_debug_info(argument):
    print_classifier_debug_info.level = 0

    def decorator(function):
        def wrapper(*args, **kwargs):
            if display:
                global level
                sArgument = argument.replace("vsg.vhdlFile.classify.", "")
                sLevel = " " * (2 * level)
                sEntering = f"Entering: {sLevel} {sArgument}.{function.__name__} "
                sEntering += "-" * (100 - len(sEntering))
                print(sEntering)
                level += 1

            results = function(*args, **kwargs)

            if display:
                sExiting = f"Exiting:  {sLevel} {sArgument}.{function.__name__} == {results} "
                sExiting += "-" * (100 - len(sExiting))
                print(sExiting)
                level -= 1

            return results

        return wrapper

    return decorator


def push_pop_seek_index(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        args[0].push_seek_index()

        results = func(*args, **kwargs)

        args[0].pop_seek_index()

        return results

    return wrapper


def push_pop_current_index(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        args[0].push_current_index()

        results = func(*args, **kwargs)

        args[0].pop_current_index()

        return results

    return wrapper
