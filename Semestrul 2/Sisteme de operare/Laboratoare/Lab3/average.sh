#!/bin/bash

if [ -z "$1" ]; then
  echo "Va rugam sa furnizati fisierul de intrare!"
  exit 1
fi

input_file="$1"
cpu_usage_sum=0
line_count=0

while read -r line; do
  cpu_usage=$(echo "$line" | awk '{print $7}' | sed 's/%//')
  
  if [[ "$cpu_usage" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    cpu_usage_sum=$(echo "$cpu_usage_sum + $cpu_usage" | bc)
    line_count=$((line_count + 1))
  fi
done < "$input_file"

if [ $line_count -gt 0 ]; then
  average_cpu_usage=$(echo "scale=2; $cpu_usage_sum / $line_count" | bc)
  echo "Media CPU Usage este: $average_cpu_usage%"
else
  echo "Nu au fost gasite valori valide pentru CPU Usage."
fi
