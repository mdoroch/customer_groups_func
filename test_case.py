from collections import Counter


def digits_sum(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def customer_groups_1(n_customers):
    count_dict = dict()
    n_customers = range(n_customers)

    for i in n_customers:
        cur_sum = 'group_' + str(digits_sum(i))
        if cur_sum in count_dict:
            count_dict[cur_sum] += 1
        else:
            count_dict[cur_sum] = 1

    return count_dict


def customer_groups_2(n_first_id, n_customers):
    count_dict = dict()
    n_customers = range(n_first_id, n_first_id + n_customers)

    for i in n_customers:
        cur_sum = 'group_' + str(digits_sum(i))
        if cur_sum in count_dict:
            count_dict[cur_sum] += 1
        else:
            count_dict[cur_sum] = 1

    return count_dict
