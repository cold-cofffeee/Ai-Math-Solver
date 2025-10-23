# Installation and Run Script for AI Math Solver
# Run this file to install dependencies and start the app

Write-Host "Installing required packages..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "`nStarting AI Math Solver..." -ForegroundColor Green
streamlit run main.py
