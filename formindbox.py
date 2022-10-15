def get_sum_digits(c: int) -> int:
    s = 0
    while c != 0:
        s += c % 10
        c //= 10
    return s


# функция номер один
def get_groups(n_customers: int) -> dict:
    d = {}
    for i in range(n_customers):
        group = get_sum_digits(i)
        d[group] = d.get(group, 0) + 1
    return d  # получим словарь, где ключ это номер группы, а значение это количество клиентов в ней


# функция номер два
def get_groups_2(n_customers: int, n_first_id: int) -> dict:
    d = {}
    for i in range(n_first_id, n_first_id+n_customers):
        group = get_sum_digits(i)
        d[group] = d.get(group, 0) + 1
    return d  # получим словарь, где ключ это номер группы, а значение это количество клиентов в ней


print(get_groups(100))
print(get_groups_2(10, 100))
