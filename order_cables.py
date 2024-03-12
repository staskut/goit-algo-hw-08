import heapq


def order_cables_heap(cables_list):
    """
    Кожне зʼєднання коштує суму довжин. Це сумується у витрати. Якщо на початку зʼєднаємо довгий кабель і будемо його
    "тягати" по наступних зʼєднаннях, то його давжина буде в витратах кілька разів. Для того щоб мінімізувати витрати,
    треба кожного разу зʼєднувати найкоротші кабелі в наявності. Для цього будемо брати два найкоротших кабелі з верху
    купи, зʼєднувати і додавати назад в купу.
    """
    cables_list = cables_list.copy()
    heapq.heapify(cables_list)
    sequence = []

    while len(cables_list) > 1:
        first = heapq.heappop(cables_list)
        second = heapq.heappop(cables_list)

        new_length = first + second
        sequence.append((first, second))

        heapq.heappush(cables_list, new_length)

    total_cost = sum([sum(pair) for pair in sequence])

    return sequence, total_cost


def order_cables_no_heap(cables_list):
    pool = cables_list.copy()
    seq = []
    while len(pool)>1:
        first, second = sorted(pool)[:2]
        seq.append((first, second))
        new = first+second
        pool.remove(first)
        pool.remove(second)
        pool.append(new)

    total_cost = sum([sum(pair) for pair in seq])

    return seq, total_cost


if __name__=="__main__":
    cables_list = [1, 2, 11, 35, 1, 223, 2, 3]
    print(order_cables_no_heap(cables_list))
    print(order_cables_heap(cables_list))
    # такі самі результати:
    # ([(1, 1), (2, 2), (2, 3), (4, 5), (9, 11), (20, 35), (55, 223)], 373)
    # ([(1, 1), (2, 2), (2, 3), (4, 5), (9, 11), (20, 35), (55, 223)], 373)

    import random, time
    cables_list = [random.randint(0, 1000) for _ in range(10000)]

    def measure(func, arg):
        start = time.time()
        func(arg)
        end = time.time()
        print(end-start)

    measure(order_cables_no_heap, cables_list)
    measure(order_cables_heap, cables_list)
    # без застосування купи набагато довше:
    # 2.846622943878174
    # 0.005431175231933594
