#!/bin/bash
pip install --no-cache-dir -r requirements.txt

# Jalankan script Python dalam sesi screen
screen -dmS my_python_script python run.py

echo "Step 1 completed"
