def remove_lines(file, line):
    with open(file, 'r+') as f:
        desired_output = f.read().replace(line + '\n', '')
        f.seek(0)
        f.write(desired_output)
        f.truncate()


filename = 'remove_lines.txt'
line_to_remove = 'line to remove'
remove_lines(filename, line_to_remove)
