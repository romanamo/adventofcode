def is_command(s: str):
    return s.startswith("$")


def get_path(path: list, folder: dict):
    if len(path) == 0:
        return folder
    return get_path(path[1:], folder[path[0]])


def parse_to_dict(rows: list[str], i: int = 0, dictio: dict = {}, path: list[str] = []):
    while i < len(rows):
        args = rows[i].split()
        if args[0] == "$":
            if args[1] == "cd":
                if args[2] == "..":
                    path.pop()
                else:
                    tmp = get_path(path, dictio)
                    path.append(args[2])
                    tmp[args[2]], i = parse_to_dict(rows, i + 1, {}, path)
            elif args[1] == "ls":
                while i + 1 < len(rows) and not is_command(rows[i + 1]):
                    ls_args = rows[i + 1].split()
                    if ls_args[0] == "dir":
                        dictio[ls_args[1]] = {}
                    else:
                        dictio[ls_args[1]] = ls_args[0]
                    i += 1
                return dictio, i
        i += 1
    return dictio, i


def sum_recursive(d: dict, summe: int = 0, back=None):
    if back is None:
        back = []
    for k, v in d.items():
        if isinstance(v, dict) and len(v) != 0:
            summe += sum_recursive(d=v, back=back)[1]
        else:
            summe += int(v)
    back.append(summe)
    return back, summe


with open("input.txt", "r") as input_file:
    lines = list(map(lambda x: x.rstrip("\n"), input_file.readlines()))
    res = parse_to_dict(rows=lines)[0]
    final = sum_recursive(res)[0][:-1]

    candidates = []
    outer = max(final)
    for i in final:
        if (70000000 - outer) + i >= 30000000:
            candidates.append(i)
    print(min(candidates))
