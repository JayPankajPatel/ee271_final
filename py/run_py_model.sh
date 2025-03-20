#!/bin/bash

VIRT_ENV="cnn"
FILE="cnn.py"

# Ensure pyenv is loaded into the shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init - bash)"
eval "$(pyenv virtualenv-init -)"

activate_virtenv() {
  pyenv activate $VIRT_ENV
}

deactivate_virtenv() {
  pyenv deactivate  # No argument needed
}

install_dependencies() {
  python -m pip install -r requirements.txt
}

run_py() {
  python "$FILE"
}

# Execute the script
activate_virtenv
install_dependencies
run_py
deactivate_virtenv
