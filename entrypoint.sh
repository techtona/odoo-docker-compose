#!/bin/bash

# Optional: pull enterprise updates (if using git)
# cd /mnt/enterprise && git pull

# Install Python requirements if requirements.txt exists
if [ -f /mnt/requirements.txt ]; then
    pip install --no-cache-dir --break-system-packages -r /mnt/requirements.txt
fi

exec odoo "$@"
