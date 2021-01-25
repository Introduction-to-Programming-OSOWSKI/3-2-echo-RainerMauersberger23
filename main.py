def echo(x, y):
    output = x
    for i in range (1, y):
        output = output + x

    return output

print (echo("hello", 5))