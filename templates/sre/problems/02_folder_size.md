# Problem 2: Calculate Folder Size

**Source:** Google SRE Interview (Glassdoor)

## Problem Statement

Given a file system where each item is either:
- A **file** with a `name` and `size`
- A **folder** containing IDs of items inside it

Write a function to calculate the total size of a folder (including all nested contents).

## Function Signature

```python
def folder_size(fs: dict, folder_id: str) -> int:
    """
    Calculate total size of a folder.
    
    fs: dict mapping id -> item
        item is either {"type": "file", "name": str, "size": int}
                   or {"type": "folder", "name": str, "children": list[str]}
    folder_id: the folder to calculate size for
    
    Returns: total size in bytes
    """
    pass
```

## Your Solution

Create your solution in `solutions/02_folder_size.py`

