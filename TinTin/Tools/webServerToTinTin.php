<?php 
$address = '127.0.0.1';

if (($socket=socket_create(AF_INET, SOCK_STREAM, SOL_TCP)) and (socket_connect($socket, $address, 3333)))
{

    sleep(1);
    $send = "I can see clearly now, the rain has come\n";
    socket_send($socket, $send, strlen($send), 0);
    $sAnswer = socket_read($socket, 1000);  
    echo "RECEIVED " .$sAnswer;
    sleep(1);

    socket_close($socket);
}
  

?>