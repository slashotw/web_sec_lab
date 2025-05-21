<?php
header('content-type:html');
if(isset($_GET['file'])){
    echo file_get_contents("file/".$_GET['file']) ;
}

?>