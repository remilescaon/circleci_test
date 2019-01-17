import json

if __name__ == '__main__':
    print('Hello World')

    print('Dumping file')
    with open('hello.json', 'w') as f:
        json.dumps('Hello World')
