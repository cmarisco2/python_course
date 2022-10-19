# Look @ decorator_fn.py for general defintion.

# 1 -> Use Higher Order Wrapper FN
# 2 -> use @ syntax vice fn = higher_order_func(fn)

def be_polite(fn):
    def wrapper():
        print('Nice to meet you')
        fn()
        print('Have a nice day')
    return wrapper


@be_polite
def greet():
    print("My Name is Chris")


@be_polite
def goodbye():
    print('Good Bye')


greet()
goodbye()
