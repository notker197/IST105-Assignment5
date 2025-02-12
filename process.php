<?php
header("Content-type: text/html");

$number = $_POST['number'];
$text = $_POST['text'];

// Ejecutar Python y capturar la salida
$output = shell_exec("python3 process.py $number $text");

echo $output;
?>