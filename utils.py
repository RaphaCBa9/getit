def extract_route(string):
    return string.split("\n")[0].split(" ")[1][1:]


def read_file(path):
    with open(path, "rb") as f:
        return f.read()
