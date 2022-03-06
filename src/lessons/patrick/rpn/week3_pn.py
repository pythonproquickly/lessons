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
        print(ps.strip())


def evaluate_postfix(postfix_expressions):
    for postfix_expression in postfix_expressions:
        stack = Stack([])
        split_exp = postfix_expression.split()
        print(split_exp)
        error = False
        for ch in split_exp:
            if ch not in ' /*+-0123456789':
                print(f"** ERROR ** in {split_exp}")
                error = True
                break
        if error:
            continue
        for ch in split_exp:
            if ch in '+-*/':
                i2 = stack.pop()
                i1 = stack.pop()
                print(i1, ch, i2)
                try:
                    print(eval('%s' * 3 % (i1, ch, i2)))
                    stack.push(eval('%s' * 3 % (i1, ch, i2)))
                except:
                    print(f"** ERROR ** in {postfix_expression}")
                    continue
            else:
                try:
                    _ = int(ch)
                except ValueError:
                    replaced_ch = ""
                    for c in ch:
                        if c in " 0123456789":
                            replaced_ch += c
                        else:
                            replaced_ch += " "
                    ch = replaced_ch
                finally:
                    stack.push(ch)

        print('result', stack.pop())


def main():
    evaluate_postfix(PFList)
    evaluate_infix(IFList)


if __name__ == "__main__":
    main()
