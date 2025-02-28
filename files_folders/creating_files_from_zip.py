from pathlib import Path
import zipfile

root_dir = Path(__file__).parent / 'files'
archive_path = root_dir / 'archive.zip'

with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.rglob("*.txt"):
        # Write the file content with a relative archive name
        zf.write(path, arcname=path.relative_to(root_dir))
        path.unlink()  # Optionally remove the file after archiving
