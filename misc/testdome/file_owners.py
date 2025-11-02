# https://www.testdome.com/d/python-interview-questions/9
"""Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
"""

class FileOwners:

    @staticmethod
    def group_by_owners(files):
        results = dict()
        for value in files.values():
            if value not in results:
                file_list = [k for k, v in files.items() if v == value]
                results[value] = file_list
        return results


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(FileOwners.group_by_owners(files))