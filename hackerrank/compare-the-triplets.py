# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
    a_score = b_score = 0

    def compare_two(x, y):
        if x == y:
            return 0, 0
        elif x > y:
            return 1, 0
        else:
            return 0, 1

    a_score += compare_two(a0, b0)[0]
    a_score += compare_two(a1, b1)[0]
    a_score += compare_two(a2, b2)[0]
    b_score += compare_two(a0, b0)[1]
    b_score += compare_two(a1, b1)[1]
    b_score += compare_two(a2, b2)[1]

    return '{0}{1}'.format(a_score, b_score)


a0, a1, a2 = 5, 6, 7
b0, b1, b2 = 3, 6, 10
print(solve(a0, a1, a2, b0, b1, b2))