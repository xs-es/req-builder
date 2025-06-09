# 🧪 Minimal Requirements Extractor

**Minimal Requirements Extractor** is a Python utility that scans your source code and generates a **precise `requirements.txt` file** containing only the third-party packages your project actually uses.

This avoids the bloat of `pip freeze` and the inconsistencies of tools like `pipreqs`, ensuring clean, reproducible dependency management — perfect for open-source releases, Docker environments, CI pipelines, and production deployments.

---

## 🔍 Why Use This?

| Tool        | Includes Unused Packages? | Requires Clean Env? | Accuracy on Used Imports | Notes                       |
|-------------|---------------------------|----------------------|---------------------------|-----------------------------|
| `pip freeze`| ✅ Yes                    | ✅ Yes               | ❌ Poor                   | Captures full environment   |
| `pipreqs`   | ❌ No                     | ❌ No                | ⚠️ Mixed                  | Static analysis-based       |
| `pip-chill` | ❌ No                     | ✅ Yes               | ❌ Misses some packages   | Doesn't detect usage        |
| ✅ This Tool| ❌ No                     | ❌ No                | ✅ Accurate               | Static + metadata analysis  |

---

## 🧠 Features

- 📂 Scans your project recursively for `import` and `from ... import` statements.
- 🚫 Ignores Python’s standard library and built-in modules.
- 📦 Resolves used imports to actual PyPI package names and installed versions.
- 🧪 Outputs a clean, optionally pinned `requirements.txt`.
- 🔒 Safe for use in both development and production environments.

---

## 📁 Repository Structure

```text
minimal-requirements/
├── extract_requirements.py    # Main analysis script
├── .gitignore                 # Optional: ignore venv, __pycache__, etc.
├── LICENSE                    # Apache 2.0 License
├── README.md                  # Full documentation
└── requirements.txt           # Auto-generated result
```

### 🚀 Quickstart

## 1. 🔁 Clone the Repository
# Using HTTPS:

```bash
git clone https://github.com/yourusername/minimal-requirements.git
cd minimal-requirements
```

# Using GitHub CLI:
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

## 2. 🧪 Create and Activate a Virtual Environment (Recommended)
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```
# Install your project's true dependencies using pip.

## 3. 🛠️ Configure the Script
# Open extract_requirements.py and set your source directory:

```python
SRC_DIR = Path("your_project_directory")
```
Replace "your_project_directory" with the relative path to your code folder. Example:
```python
SRC_DIR = Path("src/")
```
4. ▶️ Run the Script
```bash
python extract_requirements.py
```
# This will generate a clean requirements.txt with only third-party dependencies you actually imported.

## ✅ Example
# If your src/app.py contains:

```python
import numpy as np
import requests
from flask import Flask
```
The generated requirements.txt will be:

```text
Flask==2.3.3
numpy==1.26.4
requests==2.31.0
```
### ⚙️ Advanced Notes
## ❌ No need to clean your environment — script filters standard libraries and unused packages.

# 🔍 Uses importlib_metadata to ensure proper PyPI package names and version resolution.

# 🧠 Compatible with Python 3.7–3.12 and works cross-platform (Linux/macOS/Windows).

# 🔁 Works recursively — scans all .py files in subdirectories.

### 💡 Tips
# Works well with Docker builds to shrink layer size.

# Ideal for CI pipelines to audit or validate dependencies.

# Avoids production surprises caused by invisible dev dependencies.

### 🧬 FAQ
## Q: Will this pick up unused packages?
# A: No — it only includes third-party packages that your code actually imports.

## Q: Can I use it in commercial software?
# A: Yes. Licensed under Apache 2.0 — full rights granted for personal and commercial use.

## Q: What about dynamically imported packages?
# A: These aren't detected via static analysis. If you use importlib.import_module() or similar, manually include those.

## Q: What if I'm not in a virtualenv?
# A: It'll still run, but the package resolution might include system-wide packages. For best results, use a venv.

###📜 License
```pgsql
Apache License 2.0

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.  
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,  
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
See the License for the specific language governing permissions and limitations under the License.
```
See the LICENSE file for the full text.
