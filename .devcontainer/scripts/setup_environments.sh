#!/bin/bash

# Setup script to initialize uv environments for all subprojects
echo "Setting up uv virtual environments for all subprojects..."

# Get the workspace root directory (two levels up from .devcontainer/scripts)
WORKSPACE_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$WORKSPACE_ROOT"

# Directories with pyproject.toml files
PROJECTS=("kaggle" "leetcode" "codeforces")

for project in "${PROJECTS[@]}"; do
    if [ -d "$project" ] && [ -f "$project/pyproject.toml" ]; then
        echo "Setting up environment for $project..."
        cd "$project"

        # Create virtual environment and install all dependencies
        uv sync --all-extras

        echo "✓ Environment for $project is ready"
        cd ..
    else
        echo "⚠ Skipping $project (no pyproject.toml found)"
    fi
done

echo "All environments are set up!"
echo ""
echo "🎯 Use VS Code workspace for automatic environment switching:"
echo "   code pytest.code-workspace"
