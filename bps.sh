#!/bin/bash

echo "This script will use BPSRender on your .blend file in this folder. Make sure that there is only 1 .blend and that you have configured its render settings beforehand."
wd=$(pwd)
echo "Working Directory:" $wd
cd ~/bin/BPSRender/

for file in "$wd"/*; do
  if [[ $file == *.blend ]]; then
    echo "File to be processed: " $(basename $file)
    python3 -m bpsrender $file -o $wd/ -w 4 -v
  else
    echo "No .blend file found."
  fi
done
