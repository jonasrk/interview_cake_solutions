class Expression:
    # This is only an interface
    def __init__(self, first, second, sum):
        self.first = first
        self.second = second
        self.sum = sum

    def get_chars(self):
        s = set()
        for char in self.first:
            s.add(char)
        for char in self.second:
            s.add(char)
        for char in self.sum:
            s.add(char)
        return s

    def solve(self):
        chars = self.get_chars()

        def all_permutations(input):
            if len(input) == 2:
                return [[input[0], input[1]], [input[1], input[0]]]
            else:
                first = input[0]
                perms = all_permutations(input[1:])
                sols = []
                for perm in perms:
                    for i in range(0, len(perm) + 1):
                        sols.append(perm[:i] + [first] + perm[i:])
                return sols
    
        digits = []
        for i in range(0, 10):
            digits.append(i)

        digit_perms = all_permutations(digits)
       
        sols = []

        for perm in digit_perms:
            sol = {}
            for i, char in enumerate(chars):
                sol[char] = perm[i]
            if self.evaluate(sol):
                # sols.add(sol) # TODO JRK: output all sols
                return sol

        return sols

    def evaluate():
        raise ValueError("Should have implemented this.")

class AdditionExpression(Expression):
    def evaluate(self, solution):
        first_digits = ''
        for char in self.first:
            first_digits += str(solution[char])
        second_digits = ''
        for char in self.second:
            second_digits += str(solution[char])
        sum_digits = ''
        for char in self.sum:
            sum_digits += str(solution[char])

        if int(first_digits) + int(second_digits) == int(sum_digits):
            return True
        else:
            return False
        
class MultiplicationExpression(Expression):
    def evaluate(self, solution):
        first_digits = ''
        for char in self.first:
            first_digits += str(solution[char])
        second_digits = ''
        for char in self.second:
            second_digits += str(solution[char])
        sum_digits = ''
        for char in self.sum:
            sum_digits += str(solution[char])

        if int(first_digits) * int(second_digits) == int(sum_digits):
            return True
        else:
            return False

add_exp = AdditionExpression("AAA", "AAA", "ABCBA")
print(add_exp.solve())
