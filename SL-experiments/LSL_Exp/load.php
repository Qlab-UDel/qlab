<?php
$files = array(
    1=>'lsl.html',
    2=>'../SSL_Exp/ssl.html',
    3=>'../expf/deep/tsl.html',
    4=>'../expf/deep/vsl.html',
 
shuffle($files);

for($i=0;$i<3;$i++) {
    include_once("path/to/$files[$i]");
}
?>