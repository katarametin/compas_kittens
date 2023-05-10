def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    return abs(area / 2), abs(area / 2) + 100


# if __name__ == "__main__":
#     a = polygon_area(polygon)
