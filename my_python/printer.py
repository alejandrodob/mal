from _types import List, Vector

def pr_str(data_structure):
    if type(data_structure) == List:
        result = List([pr_str(elem) for elem in data_structure])
        result = '(' + " ".join(result) + ')'
    elif type(data_structure) == Vector:
        result = List([pr_str(elem) for elem in data_structure])
        result = '[' + " ".join(result) + ']'
    else:
        result = str(data_structure)
    return result
