from pathlib import Path

# Get the directory where the current script is located
script_dir = Path(__file__).parent

# Create a path relative to the script location
p1 = script_dir / 'files' / 'ghi.txt'

# Ensure the 'files' directory exists
p1.parent.mkdir(parents=True, exist_ok=True)

print(type(p1))

if not p1.exists():
    with open(p1, 'w') as file:
        file.write('Content 3')

print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = script_dir / 'files'
print(list(p2.iterdir()))
