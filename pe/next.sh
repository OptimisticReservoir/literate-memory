#!/usr/bin/env bash
echo "Making a new Project Euler file."
last_file=$(ls p* | grep [0-9]* | tail -1)
echo "Last file was "$last_file
next_num=$(expr $(echo $last_file|grep -o [0-9]*) + 1)
next_file="p"$next_num".py"
echo "Next file is "$next_file
cp ./template.py ./$next_file
git add ./$next_file
git commit -m "Created $next_file"
echo $next_file" created and added to git."
