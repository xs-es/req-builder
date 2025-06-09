# 🧪 Minimal Requirements Extractor

A Python tool to generate a clean `requirements.txt` file by scanning only the third-party packages your code actually uses. Perfect for avoiding bloated dependency lists.

---

## 🔧 Features

- Extracts real `import` usage from your codebase
- Excludes all Python standard library modules
- Resolves to actual PyPI package names
- Optionally pins versions (`==`) for reproducible installs

---

## 🚀 Getting Started

### 🔁 1. Clone the repository

```bash
git clone https://github.com/yourusername/minimal-requirements.git
cd minimal-requirements
