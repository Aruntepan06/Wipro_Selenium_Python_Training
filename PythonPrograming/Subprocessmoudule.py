# subprocess module -

# execute extenranl system commands
# iteract with OS processess
# capture output , error and return codes
# control the process execution

# run the OS level commands - linux , macos , windows

import subprocess

# subprocess.run() - run command and wait
# subprocess.Popen() - run process aynchronulsy
# subprocess.PIPE - capture the output
# subprocess.CompleteProcess - result
# subprocess.TimeoutExpired - Time outexepction
# subprocess.CalledProcessError - command failure

# subprocess.run() - run command and wait

# 1️⃣ List files (like dir in Windows → ls in macOS)
result = subprocess.run("ls", shell=True, capture_output=True, text=True)
print(result)

# 2️⃣ Network details (like ipconfig in Windows → ifconfig in macOS)
result = subprocess.run("ifconfig", shell=True, capture_output=True, text=True)
print(result)
result = subprocess.run("python3 --version", shell=True, capture_output=True, text=True)
print(result.stdout)   # Output
print(result.stderr)   # Errors (if any)