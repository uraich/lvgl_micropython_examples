#!/bin/bash
cat ../../header_unix.py $1 ../../trailer_unix.py > exec.py
chmod +x exec.py
./exec.py
