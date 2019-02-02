# Parses times from yolo log file
# $1 is the log file
# $2 is the output file
awk '/rate/ {print}' $1 | sed -n -e 's/^.*rate,//; s/seconds,.*//; s/\s*// p' > $2
