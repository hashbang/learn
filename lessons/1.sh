#!/bin/bash

cat <<EOF 

  Hi! Welcome to #! learn
  
  We will start by introducing some basics of using the shell
  
  Lets first start with the "echo" command.
  
  Try "echo Hello World"

EOF

open_pane

wait_for "Hello World"

clear

echo "  Good! Let's move on to the next lesson."
