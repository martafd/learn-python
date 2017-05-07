# decorators are like wrappers for function
def dec(func):
    def func_wrap():

        print 'Before func '
        func()
        print 'After func '
    return func_wrap
@dec
def hello():
    print 'hello world'
# hello()

# decorators are used to find executable time
import time
from random import randint

def time_ex(count):
    def wrapper(fn):
        def wrap(*args):
            times = []
            for i in xrange(count):
                start = time.time()
                res = fn(*args)
                end = time.time()
                times.append(round(end-start, 5))
            print 'Avg. time {0}s. \nMax time {1}s. \nMin time {2}s.'.format(sum(times) / count,
                                                    max(times) / count, min(times) / count)
            return res
        return wra
    return wrapper


@time_ex(3)
def slow_fn(x):
    time.sleep(randint(1000, 3000)/1000)
    return x*x

# decorators are used to check types
def typed(*types):
    def wrapper(fn):
        def wrap(*func_args):
            for i in range(len(types)):
                if type(func_args[i]) != types[i]:
                    print func_args[i]
                    raise TypeError('Not correct type!!!!')
            return fn(*func_args)
        return wrap
    return wrapper

@typed(int, int, int)
def typed_fn(x, y, z):
    return x * y * z

@typed(str, str, str)
def typed_fn2(x, y, z):
    return x + y + z

@typed(str, str, int)
def typed_fn3(x, y, z=""):
    return (x + y) * z

# decorators are used in db transactions
def transaction(db):
    def wrapper(fn):
        def wrap(*args):
            res = None
            db.start_transaction()
            try:
                res = fn(*args)
            except Exception as e:
                db.rollback()
                raise e
            else:
                db.end_transaction()
        return wrap()
    return wrapper()


@transaction(db)
def action(db):
    db.ids.insert(1/0)
