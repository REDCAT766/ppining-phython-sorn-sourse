import subprocess
import sys

# Force install PyInstaller directly inside the active Python path
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

# Trigger the compilation process directly
subprocess.check_call([
    sys.executable, "-m", "PyInstaller",
    "--clean",
    "--onefile",
    "--noconsole",
    "pal_face.py"
])

print("\n--- ok you  fucking got it i think. ---")
