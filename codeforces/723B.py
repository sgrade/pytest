# B. Text Document Analysis

n = int(input())
s = input()

longest_word_outside_parentheses = 0
num_of_words_inside_parentheses = 0

count_in = False
w_out = ""
w_in = ""


def count_words():
    global longest_word_outside_parentheses
    global num_of_words_inside_parentheses
    global w_out
    global w_in
    
    longest_word_outside_parentheses = max(longest_word_outside_parentheses, len(w_out))
    num_of_words_inside_parentheses += (1 if len(w_in) > 0 else 0)

    w_out = ""
    w_in = ""


for ch in s:
    
    if ch == '_':
        count_words()
    
    elif ch == '(':
        count_in = True
        count_words()
    
    elif ch == ')':
        count_in = False
        count_words()
    
    else:
        if count_in:
            w_in += ch
        else:
            w_out += ch

count_words()


print(longest_word_outside_parentheses, num_of_words_inside_parentheses)
