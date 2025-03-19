#!/bin/bash

# Exit script if any command fails
set -e

# Define Python version required
PYTHON_VERSION="3.10.6"
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_NAME="venv"

# Function to check if pyenv is installed
check_pyenv() {
    if command -v pyenv >/dev/null 2>&1; then
        echo "✅ pyenv is already installed."
    else
        echo "🚀 Installing pyenv (no sudo required)..."
        curl https://pyenv.run | bash

        # Add pyenv to shell configuration
        echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
        echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
        echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
        source ~/.bashrc
    fi
}

# Function to install the correct Python version using pyenv
install_python() {
    if pyenv versions | grep -q "$PYTHON_VERSION"; then
        echo "✅ Python $PYTHON_VERSION is already installed."
    else
        echo "📥 Installing Python $PYTHON_VERSION..."
        pyenv install "$PYTHON_VERSION"
    fi

    # Set local Python version for this project
    pyenv local "$PYTHON_VERSION"
}

# Function to set up virtual environment
setup_venv() {
    if [ -d "$PROJECT_DIR/$VENV_NAME" ]; then
        echo "✅ Virtual environment already exists."
    else
        echo "🐍 Creating virtual environment ($VENV_NAME)..."
        python -m venv "$PROJECT_DIR/$VENV_NAME"
    fi
}

# Function to install dependencies
install_dependencies() {
    echo "📦 Installing dependencies..."
    source "$PROJECT_DIR/$VENV_NAME/bin/activate"
    pip install --upgrade pip
    if [ -f "$PROJECT_DIR/requirements.txt" ]; then
        pip install -r "$PROJECT_DIR/requirements.txt"
    else
        echo "⚠️ No requirements.txt found. Skipping package installation."
    fi
    deactivate
}

# Run setup steps
check_pyenv
install_python
setup_venv
install_dependencies

echo "✅ Setup complete!"
echo "🔹 To activate your environment, run: source $PROJECT_DIR/$VENV_NAME/bin/activate"
echo "🔹 To deactivate, run: deactivate"
echo "🚀 Now you can run your Python project with the correct version!"

