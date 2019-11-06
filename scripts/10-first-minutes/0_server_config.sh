#!/bin/bash
echo "Running scripts 1-4 in a dependent chain"

sudo ./1.update.sh && sudo ./2.new_user.sh && sudo ./3.firewall.sh && sudo ./4.install.sh
