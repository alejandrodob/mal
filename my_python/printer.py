from _types import List, Vector, Hash, Function, String, Keyword

def pr_str(data_structure):
    if type(data_structure) == List:
        result = List([pr_str(elem) for elem in data_structure])
        result = '(' + " ".join(result) + ')'
    elif type(data_structure) == Vector:
        result = List([pr_str(elem) for elem in data_structure])
        result = '[' + " ".join(result) + ']'
    elif type(data_structure) == Hash:
        result = List([pr_str(elem) for elem in data_structure])
        result = '{' + " ".join(result) + '}'
    elif type(data_structure) == Function:
        return '#<function>'
    elif type(data_structure) == String:
        return '"' + data_structure.replace('"', '\\"') + '"'
    elif type(data_structure) == Keyword:
        return ':' + data_structure
    else:
        result = str(data_structure)
    return result
