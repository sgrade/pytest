def remove_lines(file, line_to_remove):
    with open(file, 'r+') as f:
        content = f.readlines()
        # content is a list strings now; each string ends with '\n'
        for line in content:
            # do not forget remove trailing \n before comparing
            if line.strip() == line_to_remove:
                content.remove(line)
        # go to the beginning of the file
        f.seek(0)
        # .write requires the argument to be a string
        list_to_string = ''.join(content)
        f.write(list_to_string)
        # cleaning up everything after written
        f.truncate()


line_to_remove = 'line to remove'
remove_lines('remove_lines.txt', line_to_remove)