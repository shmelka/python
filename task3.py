def my_func(arg1, arg2, arg3):
    args = [arg1, arg2, arg3]
    args.remove(min(args))
    return sum(args)

print(my_func(5, 10, 3))
