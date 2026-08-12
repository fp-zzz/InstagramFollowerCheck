# 📸 Instagram Follower Checker

A simple Python tool that compares your Instagram followers and following lists to identify non-mutual connections.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- Compare followers vs following lists instantly
- Identify users who don't follow you back
- Spot users who follow you that you don't follow
- Get quick summary statistics
- Clean, console-based output
- No API keys or credentials needed (you handle data collection)

## ⚠️ Important Notes

**This script is for personal use only.** It does **not** interact with Instagram's servers or API. You manually collect the data through Instagram's official channels and paste it into text files. This avoids violating Instagram's Terms of Service.

> ℹ️ For official data export: Go to Settings → Privacy → Download Your Information on Instagram.

## 📋 Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | 3.7 or higher |
| Operating System | Windows, macOS, or Linux |

No external dependencies needed — runs with standard library only.

## 🚀 Setup

### 1. Clone or Download

Option A: Clone from GitHub

    git clone https://github.com/fp-zzz/InstagramFollowerCheck.git 
    cd InstagramFollowerCheck 
    
Option B: Download ZIP \
Unzip and open the folder in your preferred editor

### 2. Create Text Files

Create two text files in the project root directory: 

    File Name	Description 
    followers.txt	Paste your followers list (one username per line) 
    following.txt	Paste your following list (one username per line) 

Format example: 

    user_one 
    second_user 
    third_person 

⚠️ Important:

One username per line \
No extra characters or spaces \
Case-sensitive (use lowercase to be safe) 

💻 Usage \
Basic Usage 

Open terminal/command prompt in the project folder  \
Run the script:

    python insta_check.py

   
### 3. View results in the console

### Sample Output

Loading lists...

    === INSTAGRAM FOLLOWER ANALYSIS === 
    Total followers: 245 
    Total following: 312 
    Not following back: 47 
    Follower you don't: 18

    --- PEOPLE YOU FOLLOW WHO DON'T FOLLOW BACK --- 
    @celebrity_fanpage 
    @inactive_account_2023 
    @brand_promo 
    
    --- PEOPLE WHO FOLLOW YOU BUT YOU DON'T FOLLOW BACK --- 
    @new_follower 
    @friend_request_pending 

## 📁 Project Structure

    InstagramFollowerCheck/ 
    ├── insta_check.py # Main Python script 
    ├── followers.txt # Your followers list (create this) 
    ├── following.txt # Your following list (create this) 
    └── README.md # This file

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError` | Ensure files are named exactly `followers.txt` and `following.txt` |
| `SyntaxError` | Make sure you're using Python 3.7+ |
| Empty results | Check that your text files aren't empty and have valid usernames |
| Wrong path error | Run from within the project folder, not elsewhere |

## 🔐 Privacy & Security

This script operates entirely **offline** on your local machine:

- ✅ No data sent to any servers
- ✅ No login credentials stored
- ✅ No API calls made
- ✅ All processing happens locally in memory
- ✅ Files can be deleted after analysis

## 📝 Contributing

Feel free to fork and submit pull requests. Possible improvements:
- Export results to CSV/JSON
- Add a GUI interface
- Track changes over time
- Batch processing support

## 📄 License

MIT License so please feel free to modify and share.

---

Quick Tips for Repository:

If you want to push this to GitHub properly:
Create .gitignore (prevents tracking your actual data files)

    echo "followers.txt" >> .gitignore
    echo "following.txt" >> .gitignore
    echo "*.pyc" >> .gitignore

Then commit and push

    git add .
    git commit -m "Add Instagram follower checker script"
    git push origin main

This way, your personal follower/following data won't get accidentally committed to the repo.
