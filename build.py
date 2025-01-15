import subprocess
import time

# Install dependencies
subprocess.run(["pip", "install", "--no-cache-dir", "-r", "requirements.txt"], check=True)

# Jalankan script Python di background menggunakan subprocess
with open("run.log", "w") as log_file:
    process = subprocess.Popen(["python", "run.py"], stdout=log_file, stderr=log_file)

# Tunggu hingga "Bot dan Web Server sedang berjalan..." muncul di log
log_ready = False
while not log_ready:
    with open("run.log", "r") as log_file:
        logs = log_file.read()
        if "Bot dan Web Server sedang berjalan..." in logs:
            log_ready = True
        else:
            time.sleep(1)  # Tunggu sebentar sebelum memeriksa lagi

print("Step completed")
