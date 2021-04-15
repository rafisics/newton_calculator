mkdir -p ~/.streamlit/
echo "[general]  
email = \"m.fuad.rafi@gmail.com\""  > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = true"  >> ~/.streamlit/config.toml
