def outer():
    x = 10

    def inner():
        y = 5
        return x + y

    result = inner()
    return result
print(outer())
