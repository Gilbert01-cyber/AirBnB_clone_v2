#!/usr/bin/env bash
# Sets up a web server for the deployment of web_static.

CONFIG="/etc/nginx/sites-available/default"

# Install Nginx if it is not already installed
if ! command -v nginx > /dev/null 2>&1; then
    apt-get update -y
    apt-get install -y nginx
fi

# Create the folder structure
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file to test the Nginx configuration
cat > /data/web_static/releases/test/index.html << 'HTML'
<html>
  <head>
  </head>
  <body>
    School
  </body>
</html>
HTML

# Recreate the symbolic link every time the script is run
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to the ubuntu user and group, recursively
chown -R ubuntu:ubuntu /data/

# Serve /data/web_static/current/ at /hbnb_static (only add it once)
if ! grep -q "location /hbnb_static" "$CONFIG"; then
    if grep -q "server_name _;" "$CONFIG"; then
        sed -i 's|server_name _;|server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}|' "$CONFIG"
    else
        sed -i '0,/^server {/s||server {\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n|' "$CONFIG"
    fi
fi

service nginx restart

exit 0
