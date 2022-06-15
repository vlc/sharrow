def trunc_repr(thing, n=160):
    f = n//2
    a = repr(thing)
    if len(a) < n+20:
        return a
    return a[:f] + "..." +  a[-f:]