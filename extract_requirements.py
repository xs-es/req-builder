import os
import ast
import pkgutil
import sys
from pathlib import Path

try:
    import importlib_metadata as metadata
except ImportError:
    import importlib.metadata as metadata

# Set your project directory
SRC_DIR = Path("your_project_directory")  # <-- Change this
OUTPUT_FILE = "requirements.txt"

# Get all standard library modules
stdlib_modules = {mod.name for mod in pkgutil.iter_modules()}
stdlib_builtin = set(sys.builtin_module_names)
stdlib_all = stdlib_modules.union(stdlib_builtin)

def extract_imports_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            node = ast.parse(f.read(), filename=str(file_path))
        except SyntaxError:
            return set()
    imports = set()
    for item in ast.walk(node):
        if isinstance(item, ast.Import):
            for alias in item.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(item, ast.ImportFrom):
            if item.module:
                imports.add(item.module.split('.')[0])
    return imports

all_imports = set()
for pyfile in SRC_DIR.rglob("*.py"):
    all_imports |= extract_imports_from_file(pyfile)

third_party = all_imports - stdlib_all

resolved_packages = {}
for dist in metadata.distributions():
    top_level = dist.read_text("top_level.txt")
    if not top_level:
        continue
    top_modules = set(top_level.strip().splitlines())
    if third_party & top_modules:
        pkg_name = dist.metadata["Name"]
        version = dist.version
        resolved_packages[pkg_name] = version

with open(OUTPUT_FILE, "w") as f:
    for pkg, version in sorted(resolved_packages.items()):
        f.write(f"{pkg}=={version}\n")

print(f"requirements.txt written with {len(resolved_packages)} packages.")
