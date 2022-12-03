Infinite Monkey Theorem

The theorem states that a monkey hitting keys at random on a typewriter
keyboard for an infinite amount of time will almost surely type a given text,
such as the complete works of William Shakespeare. Well, suppose we replace a
monkey with a Python function. How long would it take for a Python function to
generate just one sentence? The sentence we will go for is: “a monkey can
learn python perfectly well”.

The way we will simulate this is to write a
function that generates a string that is 35 characters long by choosing
random letters from the 26 letters in the alphabet plus space. We will
write another function that will score each generated string by comparing
the randomly generated string to the goal.

A third function will repeatedly
call generate and score, then if 100% of the letters are correct we are done.
If the letters are not correct then we will generate a whole new string.
To make it easier to follow, our program should keep track of the best string
generated so far.
