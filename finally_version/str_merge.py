def merge(name, json):
    str1 = '{"'
    str2 = '" : '
    str3 = '}'
    result = '%s%s%s%s%s' % (str1, name, str2, json, str3)

    print(result)

    return result