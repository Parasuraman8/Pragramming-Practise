<?php 
$con = mysqli_connect("localhost","root","srikrishna","oss");
$name = $_POST['name'];
$address = $_POST['address'];
$order = " insert into srecord(name,address) values ('$name','$address')";
$result = mysqli_query($con,$order);
if ($result) {
    echo("input data is succeed");
} else {
    echo("input data is fail");
}
?>