import os
import subprocess
read, write = os.pipe()
os.write(write, "stdin input here")
os.close(write)

subprocess.check_call(['your-command'], stdin=read)
