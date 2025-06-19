## install uv on OS
curl -LsSf https://astral.sh/uv/install.sh | sh

## create new project
uv init myproj

## install packages
uv add django requests "pandas>=2.3"
uv add --script: Add a dependency to a script
uv remove --script: Remove a dependency from a script

## remove package
uv remove django

## other usefully utilities
uv sync: Sync the project's dependencies with the environment.
uv lock: Create a lockfile for the project's dependencies.
uv tree: View the dependency tree for the project.
uv build: Build the project into distribution archives.
uv publish: Publish the project to a package index.

## run a python script directly w/o starting venv
uv run main.py

## install specific version of python
uv python list
uv python install 3.12

## start a new project and pin it to Python 3.12
uv init myproject
uv python pin 3.12
uv add django
uv run main.py (will automatically install py3.12 and django into venv)

## run a cli tool like Ruff
uv run tool ruff (or uvx ruff)

## update uv version to latest
uv self update

## activate virtual environment
source .venv/bin/activate