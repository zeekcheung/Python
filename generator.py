def gen():
    print('step 1')
    yield 'a'
    print('step 2')
    yield 'b'
    print('step 3')
    yield 'c'

g = gen()
next(g)
next(g)
next(g)