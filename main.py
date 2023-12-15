"""About brackets"""
import sys


def main() -> None:
    print('\nHey dude.\n Here u can try to enter the brackets and check them for the correctness in sequence of brackets.\n')
    while True:
        print('If you want leave - enter 0.')
        lisp_reference = input('...enter brackets without backspace or other symbols\n')
        is_correct = check(lisp_reference)
        if is_correct == False:
            print('enter correctly: read the text below')
            continue
        if is_cbs(lisp_reference) == True:
            answer = 'yes'
        else:
            need_to_move(lisp_reference)
            answer = 'no'
        print(f'Is the correctly sequence of brackets? -{answer}')


def check(lisp_reference) -> bool:
    if lisp_reference == '0':
            sys.exit()
    for symbol in lisp_reference:
        if symbol == '(' or symbol == ')':
            continue
        else:
            return False


def is_cbs (lisp_reference: str) -> bool:
    clone = lisp_reference
    while '()' in clone:
        clone = clone.replace('()', '')
    if clone == '':
        return True
    else:
        return False


def need_to_move(lisp_reference: str) -> int:
    k = 0
    i = 0
    for symbol in lisp_reference:
        if symbol == '(':
            k += 1
        elif symbol == ')':
            i += 1
    if k == i:
        if lisp_reference[0] == ')':
            symbol == '('
        if lisp_reference[0] == '(':
            symbol == ')'
        print(f'U can replace one bracket {symbol} in the beginning for the correct sequince of brackets.')
    elif k != i:
        print('U need to add or delete one bracket for the possibility of correct sequince of brackets.')


main()