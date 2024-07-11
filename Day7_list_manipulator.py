def add_to_list(L: list, target):
    l = L.copy()
    if target not in l:
        l.append(target)
    return l

def remove_from_list(L: list, target):
    l = L.copy()
    if target in l:
        l.remove(target)
    return l

def sort_items(L: list):
    l = L.copy()
    l.sort()
    return l

