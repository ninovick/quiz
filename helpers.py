"""Helper functions."""


def favorite(dict: dict[str, int]) -> list[str]:
    value_list = []
    key_list = []
    result = []
    for key in dict:
        value_list.append(dict[key])
        key_list.append(key)
    maximum: int = max(value_list)
    i: int = 0
    while i < len(value_list):
        if value_list[i] == maximum:
            result.append(key_list[i])
        i += 1
    return result

def delist(list: list[str]) -> str:
    result: str = ""
    i: int = 0
    while i < len(list):
        if i == 0:
            result += list[i]
        else:
            result += " and " + list[i]
        i += 1
    return result
