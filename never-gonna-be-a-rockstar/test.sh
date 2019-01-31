#!/bin/sh
rockstar-py ngbar.rock
python output.py > ngbar.awk
chmod +x ngbar.awk
./ngbar.awk