from pathlib import Path
import zipfile

root_dir = Path(__file__).parent / 'files'
destination_path = Path(__file__).parent / 'files' / 'destination'

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, 'r') as zf:
        final_path = destination_path / Path(path.stem)
        zf.extractall(path=final_path)
