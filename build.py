import subprocess

# Install dependencies
subprocess.run(["pip", "install", "--no-cache-dir", "-r", "requirements.txt"])

# Jalankan script Python di background
with open("run.log", "w") as log_file:
    process = subprocess.Popen(["python", "run.py"], stdout=log_file, stderr=log_file)

print("Step 1 completed")
