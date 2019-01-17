from operations import fibo

if __name__ == '__main__':
    print('Starting testing..')
    results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in range(12):
        assert(fibo(i) == results[i])
        print('{} : success.'.format(i))
