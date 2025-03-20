#!/bin/bash
install_pyenv(){
  curl -fsSL https://pyenv.run | bash

  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
}

install_python3.10.1(){
  source $HOME/.bashrc 
  pyenv install 3.10.1
}

set_python_version_locally(){
  pyenv local 3.10.1
}

create_python_virtual_env(){
  pyenv virtualenv cnn
}

source ./uninstall.sh
if [ -f '/apps/design_sources.sh' ]; then
    source '/apps/design_sources.sh'
fi
install_pyenv
install_python3.10.1
set_python_version_locally
create_python_virtual_env
echo "Setup Complete"
