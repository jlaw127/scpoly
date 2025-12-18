Environment setup
=====

We recommend using conda to create a new virtual environment for consistent dependency management and isolation.


# Environment Setup

We recommend using conda to create a new virtual environment for consistent dependency management and isolation.

## Quick Start

### 1. Create and Activate Environment

```bash
# Create environment (replace 'myenv' with your preferred name)
conda create -n myenv python=3.9 -y

# Activate the environment
conda activate myenv
```

### 2. Install Dependencies from YAML

```bash
# Install all dependencies from environment.yml
conda env update -f environment.yml --prune
```

## Alternative Methods

### If you don't have environment.yml:

```bash
# Create basic environment
conda create -n myenv python=3.9 -y
conda activate myenv

# Install packages individually
conda install numpy pandas scikit-learn matplotlib
pip install torch transformers
```

### Create environment.yml from existing environment:

```bash
# Export current environment to file
conda env export > environment.yml

# For better cross-platform compatibility, use:
conda env export --from-history > environment.yml
```

## Verify Installation

```bash
# Confirm environment is active (should show asterisk next to myenv)
conda info --envs

# Check Python version
python --version

# Test key imports
python -c "import numpy, torch; print('✓ Libraries loaded successfully')"
```

## Common Commands

| Command | Description |
|---------|-------------|
| `conda env list` | List all environments |
| `conda deactivate` | Exit current environment |
| `conda remove -n myenv --all -y` | Delete environment |
| `conda list` | Show installed packages |

## Sample `environment.yml`

```yaml
name: myenv
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - numpy=1.21
  - pandas>=1.3
  - scikit-learn
  - pip
  - pip:
    - torch>=1.9.0
    - transformers>=4.15
    - -e .  # Install local package in editable mode
```

