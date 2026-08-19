# 🛠️ Linux Tidy & System Toolbox

A lightweight utility script designed to clean, monitor, and optimize Linux systems without bloat. Perfect for keeping your daily driver or server lightweight.

## ✨ Features
- **Smart Cache Cleaner:** Clears out old package manager caches, thumbnail caches, and temporary files safely to free up disk space.
- **Broken Symlink Finder:** Scans directories to find and report dead or broken symbolic links.
- **Resource Health Check:** Quick overview of current RAM usage, disk partitions, and system stats.
- **Quick Backup Tool:** Easily archive specific config directories into compressed backups.

## 🚀 Getting Started
Clone the repository and make the script executable:

```bash
git clone [https://github.com/leo9841/linux-tidy.git](https://github.com/leo9841/linux-tidy.git)
cd linux-tidy
chmod +x tidy.py

## 💻 Usage

Run the tool with Python:
```bash
python3 tidy.py --clean
