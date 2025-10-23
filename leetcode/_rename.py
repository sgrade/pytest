# Replace hyphen in file name to underscore in all python files in the current directory

from pathlib import Path
from collections import defaultdict

def rename_files_with_hyphens():
    current_dir = Path(__file__).parent
    script_name = Path(__file__).name

    # Collect all Python files except the script itself
    python_files = [f for f in current_dir.glob("*.py") if f.name != script_name]

    # Group files by their target name to detect conflicts
    target_groups = defaultdict(list)
    rename_candidates = {}

    for file_path in python_files:
        if "-" in file_path.name:
            new_name = file_path.name.replace("-", "_")
            target_groups[new_name].append(file_path.name)
            rename_candidates[file_path] = new_name

    # Files that cannot be renamed due to conflicts
    cannot_rename = []

    # Check for conflicts
    for target_name, source_files in target_groups.items():
        if len(source_files) > 1:
            # Multiple files want the same target name
            cannot_rename.extend(source_files)
        elif (current_dir / target_name).exists():
            # Target name already exists and is not one of the source files
            cannot_rename.extend(source_files)

    # Perform renames for non-conflicting files
    renamed_count = 0
    for file_path, new_name in rename_candidates.items():
        if file_path.name not in cannot_rename:
            try:
                file_path.rename(current_dir / new_name)
                renamed_count += 1
            except OSError as e:
                cannot_rename.append(file_path.name)
                print(f"Error renaming {file_path.name}: {e}")

    # Write log only if there are files that couldn't be renamed
    if cannot_rename:
        with open("_rename.log", "w") as f:
            f.write("Files that could not be renamed:\n")
            for name in sorted(cannot_rename):
                f.write(f"- {name}\n")
        print(f"Renamed {renamed_count} files. {len(cannot_rename)} files could not be renamed (see _rename.log)")
    else:
        print(f"Successfully renamed {renamed_count} files. No conflicts or errors.")

if __name__ == "__main__":
    rename_files_with_hyphens()
