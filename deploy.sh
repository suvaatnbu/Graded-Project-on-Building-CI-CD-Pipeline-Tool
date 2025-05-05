#!/bin/bash

# Define variables
REPO_URL="https://github.com/suvaatnbu/Graded-Project-on-Building-CI-CD-Pipeline-Tool.git"
PROJECT_DIR="/var/www/html/simple-html-project"  # Adjust path as needed

# Check if the directory already exists
if [ -d "$PROJECT_DIR" ]; then
    echo "Directory exists, pulling the latest code..."
    cd "$PROJECT_DIR" || exit
    git pull origin main
else
    echo "Directory does not exist, cloning the repository..."
    git clone "$REPO_URL" "$PROJECT_DIR"
    cd "$PROJECT_DIR" || exit
fi

# Restart Nginx to reflect changes
echo "Restarting Nginx..."
sudo systemctl restart nginx

echo "Deployment complete!"

