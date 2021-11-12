import subprocess
import sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', 'pyinstaller'])