import sys

def dog():
    print('wouuu!')

def default():
    print('hello world.')

def main():
    if sys.argv[1] == 'dog':
        dog()
    else :
        default()

if __name__ == '__main__':
    main()
