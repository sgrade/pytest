"""Problem 2: Calculate folder size in a file system."""


def folder_size(fs: dict, folder_id: str) -> int:
    """Calculate total size of a folder including nested contents."""
    item = fs[folder_id]
    
    if item["type"] == "file":
        return item["size"]
    
    total = 0
    for child_id in item["children"]:
        total += folder_size(fs, child_id)
    return total
