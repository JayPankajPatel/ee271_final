#!/bin/bash

unset_pyenv_vars() {
  echo "🔹 Removing pyenv references from ~/.bashrc and other startup files..."

  # Remove pyenv from bashrc, bash_profile, and zshrc
  sed -i '/export PYENV_ROOT="\$HOME\/.pyenv"/d' "$HOME/.bashrc"
  sed -i '/export PYENV_ROOT="\$HOME\/.pyenv"/d' "$HOME/.bash_profile"
  sed -i '/export PYENV_ROOT="\$HOME\/.pyenv"/d' "$HOME/.profile"
  sed -i '/export PYENV_ROOT="\$HOME\/.pyenv"/d' "$HOME/.zshrc"

  sed -i '/\[\[ -d \$PYENV_ROOT\/bin \]\] && export PATH="\$PYENV_ROOT\/bin:\$PATH"/d' "$HOME/.bashrc"
  sed -i '/\[\[ -d \$PYENV_ROOT\/bin \]\] && export PATH="\$PYENV_ROOT\/bin:\$PATH"/d' "$HOME/.bash_profile"
  sed -i '/\[\[ -d \$PYENV_ROOT\/bin \]\] && export PATH="\$PYENV_ROOT\/bin:\$PATH"/d' "$HOME/.profile"
  sed -i '/\[\[ -d \$PYENV_ROOT\/bin \]\] && export PATH="\$PYENV_ROOT\/bin:\$PATH"/d' "$HOME/.zshrc"

  sed -i '/eval "\$(pyenv init --path)"/d' "$HOME/.bashrc"
  sed -i '/eval "\$(pyenv init --path)"/d' "$HOME/.bash_profile"
  sed -i '/eval "\$(pyenv init --path)"/d' "$HOME/.profile"
  sed -i '/eval "\$(pyenv init --path)"/d' "$HOME/.zshrc"

  sed -i '/eval "\$(pyenv init - bash)"/d' "$HOME/.bashrc"
  sed -i '/eval "\$(pyenv init - bash)"/d' "$HOME/.bash_profile"
  sed -i '/eval "\$(pyenv init - bash)"/d' "$HOME/.profile"
  sed -i '/eval "\$(pyenv init - bash)"/d' "$HOME/.zshrc"

  echo "✅ Removed pyenv environment variables from startup files."
}

uninstall_pyenv() {
  echo "🔹 Uninstalling pyenv..."

  # Remove pyenv root directory
  rm -rf "$HOME/.pyenv"

  # Remove bash completion files
  rm -f "$HOME/.config/bash_completion.d/pyenv.bash"
  rm -f "/etc/bash_completion.d/pyenv" 2>/dev/null

  # Run the function to remove PATH modifications
  unset_pyenv_vars

  # Unset pyenv variables in the current session
  unset PYENV_ROOT
  unset -f pyenv
  hash -r  # Refresh the command cache

  echo "✅ pyenv completely removed."
  echo "Please restart environment/terminal"
}

uninstall_pyenv
