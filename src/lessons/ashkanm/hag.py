#Write a package that exports a class "Variable"

#Call it as

from assignment import Expression, Variable

#Then provide below functionalities :

a = Variable('a')
b = Variable('b')
c = Variable('c')
a.value = 1
b.value = 2
c.value = 3

z = (a + b) * c + Variable(7) 


z.tree.assembly.eval()) --> evaluate z


assert z.tree.assembly.eval() == 16


print(z.tree))
#                   +
#                   |\
#                   * 7
#                  /|
#                 + c
#                /|
#               a b

print(z.tree.assembly))
#   PUSH a
#   PUSH b
#   ADD
#   PUSH c
#   MULT
#   PUSH 7
#   ADD
