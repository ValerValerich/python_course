# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def transponding_matrix(m):
    # res_matrix=[]
    res_matrix = zip(*m)
    # for i in range(len(m)):
    #     res_matrix.append([])
    #     for j in range(len(m[i])):
    #         res_matrix[i].append(m[j][i])
    return res_matrix


# print(*transponding_matrix(matrix), sep='\n')

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление

def keysly_arguments_function(**kwargs):
    res_dict = {}
    for k, v in kwargs.items():
        try:
            hash(v)

        except Exception:
            v = str(v)
        res_dict[v] = k
    return res_dict


print(keysly_arguments_function(one=1, two='2', three=[3, 3, 3]))
