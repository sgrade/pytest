import re


def practice_re(filename, pattern_to_search):

    p = re.compile(pattern_to_search)

    with open(filename, 'r') as f:
        file_as_a_string = f.read()

        re_search = p.search(file_as_a_string)
        print(re_search.group())
        print(re_search.start())
        print(re_search.end())
        print(re_search.span(), '\n')

        find_all = p.findall(file_as_a_string)
        print(find_all, '\n')

        find_iter = p.finditer(file_as_a_string)
        print(type(find_iter))
        for item in find_iter:
            print(item)
            print('\n')

        # Search and replace
        f.seek(0)
        new_pattern = '174.255.255.0/0'
        string_to_process = f.read()
        new_string = p.sub(new_pattern, string_to_process)
        print(new_string)


file = 'regular_expressions.config'
pattern = 'route 174.100...+[0-9]'

practice_re(file, pattern)