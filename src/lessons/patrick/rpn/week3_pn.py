class Stack:
    def __init__(self, the_stack):
        self.__the_stack = the_stack

    def push(self, item):
        self.__the_stack.append(item)

    def pop(self):
        if len(self.__the_stack) > 0:
            popped = self.__the_stack[-1]
            del self.__the_stack[-1]
        else:
            popped = ""
        return popped


PFList = ('7 5 +',
          '7 5 -',
          '7 5 *',
          '7 5 /',
          '8 4 @',
          '8 4 / 2 * 3 +',
          '8 4 / 2 * 3 *',
          '6 8 4 / 2 * 4 + -',
          '100 100 * 20 /',
          '200 w * 10 +',
          '7 6 15 11 2 * + * 20 + -',
          '3 4 5 * + * 6 + ',
          '10 20 30 40 * + * 50 +')

IFList = ('7 + 5 ',
          '7 - 5 ',
          '7 * 5 ',
          '15 / 5 ',
          '8 $ 4 ',
          '8 / 4 * 2 + 3 ',
          '8 / 4 + 2 * 3 ',
          '16 - 8 / 4 * 2 * 4 ',
          '100 * 100 / 20 + 55 ',
          '200 w * 10 +',
          '( 4 + 5 * 3 ) - 6',
          '( 3 * ( 4 + 5 ) + 6 ',
          '( ( 30 * 40 ) + 20 ) * 10 + 50 ')


def evaluate_infix(postfix_expressions):
    for expression in postfix_expressions:
        stack = []
        ps = ""
        p = {"+": 3, "-": 3, "x": 2, "/": 2, "^": 1}
        for exp_element in expression:
            if exp_element in p:
                while len(stack) != 0 and stack[-1] != "(" and p[stack[-1]] <= \
                        p[exp_element]:
                    ps += stack[-1] + " "
                    stack.pop(-1)
                stack.append(exp_element)
            elif exp_element == "(":
                stack.append("(")
            elif exp_element == ")":
                while len(stack) != 0 and stack[-1] != "(":
                    ps += stack[-1] + " "
                    stack.pop(-1)
                if len(stack) != 0:
                    stack.pop(-1)
            else:
                ps += exp_element
        while len(stack) != 0:
            ps += stack.pop(-1)
        ps = ps.strip()
        error = False
        for char in ps:
            if char not in " 0123456789*/+-()" or (
                    len(char) > 1 and not isinstance(char, int)):
                print(f"** ERROR ** in {ps}")
                error = True
                break
        if not error:
            error = False
            print(ps)


def evaluate_postfix(postfix_expressions):
    for postfix_expression in postfix_expressions:
        stack = Stack([])
        split_exp = postfix_expression.split()
        print(split_exp)
        error = False
        for exp_char in split_exp:
            if exp_char not in ' /*+-0123456789':
                print(f"** ERROR ** in {split_exp}")
                error = True
                break
        if error:
            continue
        for exp_char in split_exp:
            if exp_char in '+-*/':
                num2 = stack.pop()
                num1 = stack.pop()
                print(num1, exp_char, num2)
                try:
                    print(eval('%s' * 3 % (num1, exp_char, num2)))
                    stack.push(eval('%s' * 3 % (num1, exp_char, num2)))
                except:
                    print(f"** ERROR ** in {postfix_expression}")
                    continue
            else:
                stack.push(exp_char)
        print('result', stack.pop())


def main():
    evaluate_postfix(PFList)
    evaluate_infix(IFList)


if __name__ == "__main__":
    main()

"""Output follows:
['7', '5', '+']
7 + 5
12
result 12
['7', '5', '-']
7 - 5
2
result 2
['7', '5', '*']
7 * 5
35
result 35
['7', '5', '/']
7 / 5
1.4
result 1.4
['8', '4', '@']
** ERROR ** in ['8', '4', '@']
['8', '4', '/', '2', '*', '3', '+']
8 / 4
2.0
2.0 * 2
4.0
4.0 + 3
7.0
result 7.0
['8', '4', '/', '2', '*', '3', '*']
8 / 4
2.0
2.0 * 2
4.0
4.0 * 3
12.0
result 12.0
['6', '8', '4', '/', '2', '*', '4', '+', '-']
8 / 4
2.0
2.0 * 2
4.0
4.0 + 4
8.0
6 - 8.0
-2.0
result -2.0
['100', '100', '*', '20', '/']
** ERROR ** in ['100', '100', '*', '20', '/']
['200', 'w', '*', '10', '+']
** ERROR ** in ['200', 'w', '*', '10', '+']
['7', '6', '15', '11', '2', '*', '+', '*', '20', '+', '-']
** ERROR ** in ['7', '6', '15', '11', '2', '*', '+', '*', '20', '+', '-']
['3', '4', '5', '*', '+', '*', '6', '+']
4 * 5
20
3 + 20
23
 * 23
** ERROR ** in 3 4 5 * + * 6 + 
 + 6
6
result 6
['10', '20', '30', '40', '*', '+', '*', '50', '+']
** ERROR ** in ['10', '20', '30', '40', '*', '+', '*', '50', '+']
7  5 +
7  5 -
7 * 5
15  5 /
** ERROR ** in 8 $ 4
8  4 * 2 /  3 +
8  4 /  2 * 3 +
16  8  4 * 2 * 4 /-
100 * 100  20 /  55 +
** ERROR ** in 200 w * 10 +
4  5 * 3 +   6-
3 *  4  5 +   6 +(
30 * 40   20 +  * 10  50 +
"""
