import sys

'''A module for generating exceptions'''

def convert(s):
    ''' Convert to an integer'''
    x = -1
    try:
        x = int(s)
        print("Conversion succeeded! x = ", x)
    except (ValueError, TypeError) as e:
        print("Conversion error {}" .format(str(e)), file=sys.stderr)
    return -1

if __name__ == '__main__':
    value = convert((sys.argv[1]))