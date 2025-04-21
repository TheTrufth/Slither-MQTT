# Slither.io clone using MQTT

# Setup
- Download pyenv 
  - `brew install pyenv`
  - `brew install pyenv-virtualenv`
- Add this to `.zprofile`
  ```
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init --path)"
   ```
- Add this to `.zshrc`
  ```
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  ```
- Restart your shell
- Create the env
  - `pyenv virtualenv 3.13.3 slither-mqtt`
- Activate the env
  - `pyenv activate slither-mqtt` # To deactivate replace with activate.
- Install requirements
  - `pip install -r requirements.txt`

# Stack
- Graphics: `pygame`
- Messaging: `paho-mqtt`
- Language: Python
- Broker: `test.mosquitto.org`
