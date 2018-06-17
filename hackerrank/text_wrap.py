# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap


def wrap(string, max_width):
    wrapped_list = textwrap.wrap(string, max_width)
    output = "\n".join(wrapped_list)

    return output


input_s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
input_w = 4
result = wrap(input_s, input_w)
print(result)
