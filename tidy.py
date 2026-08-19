#!/usr/bin/env python3
import os
import shutil
import sys

def show_banner():
    print("=" * 40)
    print("     🐧 Linux Tidy & Toolbox v1.0")
    print("=" * 40)

def check_disk():
    print("\n[*] Checking Disk Space Usage...")
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // (2**30)} GB")
    print(f"Used:  {used // (2**30)} GB")
    print(f"Free:  {free // (2**30)} GB")

def clean_tmp():
    print("\n[*] Cleaning temporary files...")
    tmp_dir = "/tmp"
    if os.path.exists(tmp_dir):
        count = 0
        for item in os.listdir(tmp_dir):
            item_path = os.path.join(tmp_dir, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                    count += 1
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    count += 1
            except Exception as e:
                pass
        print(f"[+] Cleared {count} items from /tmp safely.")
    else:
        print("[-] /tmp directory not accessible.")

if __name__ == "__main__":
    show_banner()
    if len(sys.argv) > 1 and sys.argv[1] == "--clean":
        clean_tmp()
    else:
        check_disk()
        print("\nTip: Run with '--clean' to clear temporary files.")
      
