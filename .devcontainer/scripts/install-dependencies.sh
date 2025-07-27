#!/usr/bin/env bash

# Installing uv
# https://docs.astral.sh/uv/getting-started/installation/
curl -LsSf https://astral.sh/uv/install.sh | sh
# Shell autocompletion
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc

# Setup all project environments
cd /workspaces/pytest
./.devcontainer/scripts/setup_environments.sh
