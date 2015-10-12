def pr_str(data_structure):
    if type(data_structure) == list:
        result = [pr_str(elem) for elem in data_structure]
        result = '(' + " ".join(result) + ')'
    else:
        result = str(data_structure)
    return result
