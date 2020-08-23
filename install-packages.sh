#!/bin/bash

set -euo pipefail

# Disable Prompt for manual feedback
export DEBIAN_FRONTEND=noninteractive

# Update Package listing and Upgrade the packages
apt update
apt upgrade -y

# Install new packages
apt install -y --no-install-recommends python3 python3-pip

# Delete cached files and remove package listings
apt clean
rm -rf /var/lib/apt/lists/*