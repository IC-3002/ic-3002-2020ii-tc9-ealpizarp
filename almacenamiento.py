
def maximizar(As, D):
    archivos_asc = sorted(As, key=lambda tup: tup[1])
    res = []
    current_storage = 0
    for _file in archivos_asc:
        if (_file[1] + current_storage) < D:
            res.append(_file)
            current_storage += _file[1]
        else:
            break
    return res
