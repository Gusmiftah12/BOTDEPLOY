#!/bin/bash
pip install --no-cache-dir -r requirements.txt
nohup python run.py &
echo "Step 1 completed"
