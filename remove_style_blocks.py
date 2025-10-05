import os
import re

def remove_style_blocks_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = re.sub(r"<style.*?>.*?</style>", "", content, flags=re.DOTALL | re.IGNORECASE)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

def process_directory(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                remove_style_blocks_from_file(filepath)
                print(f"✅ Cleaned: {filepath}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    process_directory(base_dir)
    print("\n🎉 All <style> blocks removed successfully!")
