#!/bin/bash
cat ../../header.py $1 ../../footer.py > exec.py
chmod +x exec.py
./exec.py
