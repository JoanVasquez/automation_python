from pathlib import Path

# Get the directory of the current script and then the "files" folder within it
root_dir = Path(__file__).parent / 'files'
file_paths = root_dir.iterdir()
print(Path.cwd())

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    path.rename(new_filepath)
