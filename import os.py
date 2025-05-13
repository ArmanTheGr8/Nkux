import os
import sys
import subprocess

def auto_build_exe():
    # If already running from .exe, do nothing
    if getattr(sys, 'frozen', False):
        return

    # Only build if not already built
    exe_name = os.path.splitext(os.path.basename(__file__))[0] + '.exe'
    if os.path.exists(f"dist/{exe_name}"):
        return

    print("Creating .exe...")
    result = subprocess.run([
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--noconfirm",
        os.path.basename(__file__)
    ])

    if result.returncode == 0:
        print(f"✅ Build succeeded! Run it from dist/{exe_name}")
    else:
        print("❌ Build failed.")
    sys.exit()

auto_build_exe()

# Your actual script logic here
print("Hello, this is the main script logic.")
