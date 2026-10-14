def is_valid_corp_id(value):
    if not isinstance(value, str):
        return False
    if not value.startswith("CORP-"):
        return False
    if len(value) != 10:
        return False
    return value[5:].isdigit()


# Examples
print(is_valid_corp_id("CORP-12345"))  # True
print(is_valid_corp_id("CORP-abcde"))  # False
print(is_valid_corp_id("CORP-1234"))   # False
print(is_valid_corp_id("ABC-12345"))   # False
print(is_valid_corp_id(12345))         # False
