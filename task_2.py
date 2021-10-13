import functools

def remove_from_list(data: list, pred: callable) -> list:
    it_valid_data = 0
    for it in range(len(data)):
        if not pred(data[it]):
            if it != it_valid_data:
                data[it], data[it_valid_data] = data[it_valid_data], data[it]
            it_valid_data += 1
    return data[:it_valid_data]

remove_zero = functools.partial(remove_from_list, pred=(0).__eq__)


if __name__ == '__main__':
    from random import randint
    #test data
    data = [randint(-3, 3) for _ in range(20)]
    #usage
    print(remove_zero(data))
