# Graded Project on Building CI/CD Pipeline Tool

This project demonstrates a basic CI/CD pipeline using:

- Bash scripting
- Python (GitHub API integration)
- Cron jobs
- GitHub for version control
- Nginx for deployment on AWS EC2

## Features

- Auto-checks for new commits
- Automatically pulls and deploys changes
- Live HTML updates via Nginx

## Folder Structure


## Deployment

```bash
# Run Python script manually
python3 check_commits.py

---

## ✅ Add & Push to GitHub

```bash
git add README.md
git commit -m "Add README"
git push origin main
# Graded-Project-on-Building-CI-CD-Pipeline-Tool
# CI/CD Pipeline Project

This project demonstrates a simple Continuous Integration and Continuous Deployment (CI/CD) pipeline for a static website hosted on an AWS EC2 instance using:

- 🐍 Python (GitHub API)
- 🖥️ Bash scripting
- ⏲️ Cron jobs
- 🌐 Nginx server
- ☁️ AWS EC2
- 🔧 Git and GitHub

## 🚀 Features

- Automatically checks for new commits in a GitHub repository
- Pulls latest changes to EC2 instance
- Restarts Nginx to reflect updates
- Fully automated via cron job running every 5 minutes

## 📁 Project Structure


## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/suvaatnbu/Graded-Project-on-Building-CI-CD-Pipeline-Tool.git
cd Graded-Project-on-Building-CI-CD-Pipeline-Tool
sudo apt update
sudo apt install nginx
sudo cp index.html /var/www/html/
sudo systemctl restart nginx
crontab -e
*/5 * * * * /usr/bin/python3 /home/ubuntu/Graded-Project-on-Building-CI-CD-Pipeline-Tool/check_commits.py >> /tmp/commit_check.log 2>&1

---

Would you like me to create and commit this `README.md` for you automatically via a shell command list?

