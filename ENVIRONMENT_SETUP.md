# Simple Python Environment Management with uv

## Overview
The workspace has 3 isolated Python environments managed by uv with automatic VS Code integration:
- **kaggle/** - Data science and ML packages
- **leetcode/** - Algorithm practice tools
- **codeforces/** - Competitive programming essentials

VS Code automatically switches environments based on which folder you're working in.

## How It Works ✨

**VS Code Integration**: Open `pytest.code-workspace` and VS Code automatically uses the correct Python interpreter based on the active folder.

**Terminal Usage**: Simple manual activation when needed:
```bash
cd kaggle && source .venv/bin/activate     # For data science
cd leetcode && source .venv/bin/activate   # For leetcode practice
cd codeforces && source .venv/bin/activate # For competitive programming
```

**Direct Execution**: Run commands without activation:
```bash
uv run --directory kaggle python script.py
uv run --directory leetcode python solution.py
uv run --directory codeforces python contest.py
```

## Environment Details

| Project | Purpose | Key Packages | Dev Tools |
|---------|---------|--------------|-----------|
| **kaggle** | Data Science & ML | pandas, numpy, scikit-learn, xgboost, catboost, matplotlib, seaborn, jupyter | ruff, black, pytest, mypy |
| **leetcode** | Algorithm Practice | typing-extensions, jupyter, ipython | ruff, black, pytest, mypy, pytest-benchmark |
| **codeforces** | Competitive Programming | numpy, sympy, ipython | ruff, black, pytest, mypy |

**Standardized Dev Tools** (available in all environments):
- 🚀 **ruff** - Ultra-fast Python linter and formatter
- 🎨 **black** - Opinionated code formatter
- 🧪 **pytest** - Testing framework
- 🔍 **mypy** - Static type checker

## Getting Started

### 1. **Open VS Code Workspace** (Recommended)
```bash
code pytest.code-workspace
```
- Open any file in kaggle/ → automatically uses kaggle environment
- Open any file in leetcode/ → automatically uses leetcode environment
- Open any file in codeforces/ → automatically uses codeforces environment
- Zero manual switching required!

### 2. **Terminal Work** (When Needed)
```bash
# Data science work
cd kaggle
source .venv/bin/activate
python analysis.py
jupyter lab

# Algorithm practice
cd leetcode
source .venv/bin/activate
python solution.py
pytest test_solution.py

# Competitive programming
cd codeforces
source .venv/bin/activate
python contest.py
```

### 3. **Adding Packages**
```bash
cd kaggle        # or leetcode/codeforces
uv add requests  # Add any package you need
```

### 4. **Code Quality & Development Tools**
Use the standardized dev tools in any environment:
```bash
# Format code with black
cd kaggle && uv run black *.py

# Lint and auto-fix with ruff (super fast!)
cd leetcode && uv run ruff check --fix *.py

# Type checking with mypy
cd codeforces && uv run mypy *.py

# Run tests with pytest
cd leetcode && uv run pytest test_*.py

# Performance testing (leetcode specific)
cd leetcode && uv run pytest --benchmark-only
```

### 5. **Direct Execution** (No Activation)
```bash
uv run --directory kaggle jupyter lab
uv run --directory leetcode python solution.py
uv run --directory codeforces python contest.py
```

## Verification

Test that everything works:

**In VS Code**:
- Open `pytest.code-workspace`
- Open any `.py` file in kaggle folder
- Check bottom-left status bar shows: `3.13.5 ('.venv': venv) uv`

**In Terminal**:
```bash
cd kaggle && source .venv/bin/activate
which python
# Should show: /workspaces/pytest/kaggle/.venv/bin/python

python -c "import pandas; print('✅ Kaggle environment works!')"
```

**Dev Tools Test**:
```bash
cd leetcode
uv run ruff --version    # Should show: ruff 0.12.5
uv run black --version   # Should show: black, 25.1.0
uv run pytest --version # Should show: pytest 8.4.1
uv run mypy --version    # Should show: mypy 1.17.0
```

## Extensions & Recommendations

The workspace includes recommended VS Code extensions:
- **ms-python.python** - Core Python support
- **ms-python.black-formatter** - Black code formatter integration
- **ms-python.mypy-type-checker** - MyPy type checking integration

These extensions work seamlessly with the standardized dev tools in each environment.

---

## Relevant Files
- ✅ `pytest.code-workspace` - Multi-root VS Code workspace with extension recommendations
- ✅ `kaggle/.vscode/settings.json` - Clean environment configuration for kaggle
- ✅ `leetcode/.vscode/settings.json` - Clean environment configuration for leetcode
- ✅ `codeforces/.vscode/settings.json` - Clean environment configuration for codeforces
- ✅ `kaggle/pyproject.toml` - Kaggle dependencies + standardized dev tools
- ✅ `leetcode/pyproject.toml` - LeetCode dependencies + standardized dev tools
- ✅ `codeforces/pyproject.toml` - Codeforces dependencies + standardized dev tools
- ✅ `kaggle/environment_demo.ipynb` - Demo notebook
