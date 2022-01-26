import sys

def dog():
    print('woof!')

def default():
    print('hello world.')

def cat( ):
    print('Meeo.')

def main():

    if sys.argv[1] == 'dog':
        dog()
    elif sys.argv[1] == 'cat':
        cat()
    else:
        default()

if __name__ == '__main__':
    main()
