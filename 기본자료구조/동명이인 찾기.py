def find_same(a):
    dict = {}
    for name in a:
        if name in dict:
            dict[name] += 1
        else:
            dict[name] = 1

    result = set()

    for name in dict:
        if dict[name] >= 2:
            result.add(name)

    return result

name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same(name))