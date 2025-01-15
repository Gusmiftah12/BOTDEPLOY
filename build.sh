#!/bin/bash
pip install --no-cache-dir -r requirements.txt

# Jalankan script Python di background dan lepaskan dari shell
python run.py & disown

echo "Step 1 completed"
