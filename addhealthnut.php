<?php

$questions =$_GET['questions'];
$answers =$_GET['answers'];
$category=$_GET['category'];

$fp = fopen("./Nutrients.csv", 'a');  //Open file for append
//fwrite($fp, $row1.",".$row2); //Append row,row to file
fputcsv($fp, array($questions,$answers,$category));
fclose($fp); //Close the file to free memory.
?>
