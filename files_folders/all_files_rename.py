from pathlib import Path

root_dir = Path(__file__).parent / 'files'

for path in root_dir.glob("**/*"):
    if path.is_file():
        parent_folder = path.parts
        subfolders = path.parts[1:-1]

        new_filename = "-".join(subfolders) + '-' + path.name
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)
