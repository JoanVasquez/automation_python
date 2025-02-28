from pathlib import Path

root_dir = Path(__file__).parent / 'files'

for path in root_dir.rglob("*.txt"):
    if path.is_file():
        new_filepath = path.with_suffix(".csv")
        path.rename(new_filepath)
