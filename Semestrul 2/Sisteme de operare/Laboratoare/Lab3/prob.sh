!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <input_file>"
  exit 1
fi

input_file=$1

if [ ! -f "$input_file" ]; then
  echo "Fisierul $input_file nu exista."
  exit 1
fi

while IFS= read -r line; do
  if [[ "$line" == "ID Image_Name Name IP_Address Date Username System_Load CPU_Usage Memory_Usage Disk_Space" ]]; then
    continue
  fi

  IFS=' ' read -r id image_name name ip_address date username system_load cpu_usage memory_usage disk_space <<< "$line"
  
  echo "$id $image_name $name $ip_address $date $username $system_load $cpu_usage $memory_usage $disk_space"
done < "$input_file"
