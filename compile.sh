#!/bin/bash
gcc -c -fPIC $1.c -o $1.o
gcc -shared -Wl,-soname,lib$1.so -o lib$1.so $1.o
