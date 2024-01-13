def find_common_elements(*lists):
    return list(set.intersection(*map(set, lists)))

