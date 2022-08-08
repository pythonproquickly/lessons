import sys

from crossword import *


class CrosswordCreator():
    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable, words in self.domains.items():
            inconsistent = []
            [inconsistent.append(word) for word in words if variable.length != len(word)]
            [self.domains[variable].remove(word) for word in inconsistent]

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False

        if self.crossword.overlaps[x, y] is not None:
            x_overlap = self.crossword.overlaps[x, y][0]
            y_overlap = self.crossword.overlaps[x, y][1]
            incompatible = []
            for x_word in self.domains[x]:
                letter = x_word[x_overlap]
                compatible = []
                [compatible.append(y_word) for y_word in self.domains[y] if y_word[y_overlap] == letter]

                if len(compatible) == 0:
                    incompatible.append(x_word)
                    revised = True

            [self.domains[x].remove(word) for word in incompatible]

        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:
            arcs = []
            [arcs.append(arc) for arc in self.crossword.overlaps.keys() if arc is not None]

        while arcs:
            x, y = arcs.pop()
            if self.revise(x, y):
                if self.domains[x] is None:
                    return False
                for neighbor in self.crossword.neighbors(x):
                    if neighbor is not y:
                        arcs.append((neighbor, x))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(assignment) == len(self.domains):
            return True
        else:
            return False

    def check_length(self, variable, word):
        if variable.length == len(word):
            return True
        else:
            return False

    def check_uniqueness(self, assignment):
        difference = len([item for item in assignment.values() if item is not None]) - \
                     len(set([item for item in assignment.values() if item is not None]))

        if difference == 0:
            return True
        else:
            return False

    def check_arc_consistency(self, assignment):
        for x in assignment.keys():
            for y in assignment.keys():

                if y in self.crossword.neighbors(x):
                    if assignment[x][self.crossword.overlaps[x, y][0]] != \
                            assignment[y][self.crossword.overlaps[x, y][1]]:
                        return False
        return True

    def check_node_consistency(self, assignment):
        for variable, word in assignment.items():
            if variable.length != len(word):
                return False
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        results = []
        for key, value in assignment.items():
            if value is not None:
                node_consistency = self.check_node_consistency(assignment)
                uniqueness = self.check_uniqueness(assignment)
                arc_consistency = self.check_arc_consistency(assignment)
                if node_consistency is True and uniqueness is True and arc_consistency is True:
                    results.append(True)
                else:
                    results.append(False)

        if False in results:
            return False
        else:
            return True

    def eliminated_possibilities(self, var, word):
        eliminated = 0
        for neighbor in self.crossword.neighbors(var):
            x = word[self.crossword.overlaps[var, neighbor][0]]
            y_pos = self.crossword.overlaps[var, neighbor][1]
            eliminated += len([word for word in self.domains[neighbor] if word[y_pos] != x])

        return word, eliminated


    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        unordered_values = []
        [unordered_values.append(self.eliminated_possibilities(var, word)) for word in self.domains[var]]
        ordered_values = sorted(unordered_values, key=lambda t: t[1])

        return ordered_values

    def domain_info(self, var):
        length = len(self.domains[var])
        degree = len(self.crossword.neighbors(var))
        return var, length, degree

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned = []
        [unassigned.append(self.domain_info(var)) for var in self.domains if var not in assignment]
        sorted_unassigned = sorted(unassigned, key=lambda t: (t[1], t[2]))
        return sorted_unassigned[0][0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment

        else:
            var = self.select_unassigned_variable(assignment)
            for value in self.order_domain_values(var, assignment):
                new_assignment = assignment.copy()
                new_assignment[var] = value[0]
                if self.consistent(new_assignment):
                    result = self.backtrack(new_assignment)  
                    if result is not None:
                        return result
            return None


def main():
    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()