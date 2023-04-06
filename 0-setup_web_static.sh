
Web servers setup script.


Masilo Kgobodi
Write a Bash script that sets up your web servers for the deployment of web_static. It must:

Install Nginx if it not already installed
Create the folder /data/ if it doesn’t already exist
Create the folder /data/web_static/ if it doesn’t already exist
Create the folder /data/web_static/releases/ if it doesn’t already exist
Create the folder /data/web_static/shared/ if it doesn’t already exist
Create the folder /data/web_static/releases/test/ if it doesn’t already exist
Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
Use alias inside your Nginx configuration
Tip
Your program should always exit successfully. Don’t forget to run your script on both of your web servers.

Here's a Bash script that meets the requirements:

bash
Copy code
#!/usr/bin/env bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories if they don't already exist
mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing purposes
echo "<html><body>Hello World!</body></html>" > /data/web_static/releases/test/index.html

# Create symbolic link and update ownership
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
echo "server {
    listen 80;
    listen [::]:80;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
}" > /etc/nginx/sites-available/default

# Restart Nginx
systemctl restart nginx

exit 0
