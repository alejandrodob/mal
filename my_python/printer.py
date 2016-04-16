from _types import List, Vector, Hash, Function, String, Keyword

def pr_str(data_structure, print_readably=True):
    if type(data_structure) == List:
        result = List([pr_str(elem, print_readably) for elem in data_structure])
        result = '(' + " ".join(result) + ')'
    elif type(data_structure) == Vector:
        result = List([pr_str(elem, print_readably) for elem in data_structure])
        result = '[' + " ".join(result) + ']'
    elif type(data_structure) == Hash:
        result = List([pr_str(elem, print_readably) for elem in data_structure])
        result = '{' + " ".join(result) + '}'
    elif type(data_structure) == Function:
        return '#<function>'
    elif type(data_structure) == String:
        if print_readably:
            return '"' + data_structure.encode('unicode_escape').decode('latin1').replace('"', '\\"') + '"'
        return data_structure
    elif type(data_structure) == Keyword:
        return ':' + data_structure
    elif data_structure is True:
        return 'true'
    elif data_structure is False:
        return 'false'
    elif data_structure is None:
        return 'nil'
    else:
        result = str(data_structure)
    return result
