string1 = "buBa2144.rc1.tgz"
string2 = "v2144.rc1.tgz"

da_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = (string1.lstrip(da_chars))
result2 = (string2.lstrip(da_chars))

if(result == result2):
    print(result, "and", result2)
    print("These are duplicate releases")
else:
    print(result, "and", result2)
    print("These are not duplicate releases")