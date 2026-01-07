#!/bin/bash
set -e  # Exit immediately if a command fails

# Move to the script directory (ensures paths are correct)
cd $(dirname "$0")

echo "Installing Python dependencies..."
python3 -m pip install --upgrade pip
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Migrations are tricky on Vercel serverless
# Commented out for build, run manually if needed:
# echo "Running migrations..."
# python manage.py migrate --noinput

echo "Build script finished successfully."
