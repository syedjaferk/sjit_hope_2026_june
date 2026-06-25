def addition(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


result = addition(1, 2, 3, a=4, b=5)
print(result)
