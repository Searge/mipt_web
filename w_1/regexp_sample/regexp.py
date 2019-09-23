def calculate(data, findall):
    matches = findall(r"([abc])([+-]?)=([abc]?)([+-]?\d*)")
    # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:
        if not s:
            data[v1] = data.get(v2, 0) + int(n or 0)
        elif (s == '+'):
            data[v1] = data[v1] + data.get(v2, 0) + int(n or 0)
        elif (s == '-'):
            data[v1] = data[v1] - data.get(v2, 0) - int(n or 0)

    return data
