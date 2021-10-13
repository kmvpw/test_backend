if __name__ == '__main__':
    test_list1 = [i for i in range(-200, 200)]
    test_list2 = [i for i in range(200)]
    print(list(set(test_list1) - set(test_list2)))
