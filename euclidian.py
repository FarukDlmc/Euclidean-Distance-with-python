import math

def euclidean_distance(point1, point2):
    """
    İki nokta arasındaki Öklid mesafesini hesaplar.
    :param point1: Birinci nokta (x1, y1, z1, ...)
    :param point2: İkinci nokta (x2, y2, z2, ...)
    :return: Öklid mesafesi
    """
    distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))
    return distance

# Örnek kullanım
point1 = (1, 2, 3)
point2 = (4, 5, 6)
print(f"Öklid Mesafesi: {euclidean_distance(point1, point2)}")
