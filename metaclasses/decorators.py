
import time


def tracer(func):
    calls = 0
    def on_call(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"Calls {calls}th to {func.__name__!r}")
        return func(*args, **kwargs)
    return on_call


def timer(label="", want_trace=True):
    def on_decorator(func):
        def on_call(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed_time = time.perf_counter() - start
            on_call.alltime += elapsed_time
            if want_trace:
                funcname, alltime = func.__name__, on_call.alltime
                print(f"{label} {funcname}: {elapsed_time}, {alltime:.3f} ms")
            return result
        on_call.alltime = 0.0
        return on_call
    return on_decorator


def tester(a_class):
    sue = a_class("Sue Jones", 32, 100_000)
    bob = a_class("Bob Smith", 35, 130_000)
    print(f"{sue.name=}, {bob.name=}")
    sue.give_raise(.20)
    print(f"{sue.pay=:,.2f}, {bob.pay=}")
    print("Last Name: ", sue.get_last_name(), bob.get_last_name())

