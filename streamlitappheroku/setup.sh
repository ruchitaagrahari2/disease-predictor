#!/bin/bash

mkdir -p ~/.streamlit/

# Create credentials.toml
cat <<EOL > ~/.streamlit/credentials.toml
[general]
email = "your-email@domain.com"
EOL

# Create config.toml
cat <<EOL > ~/.streamlit/config.toml
[server]
headless = true
enableCORS = false
port = ${PORT:-8501}
EOL
