<?php 
include("auth.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashborad -client area</title>
</head>
<body>

<div class="form">
    <p>hey <?php echo $_SESSION['username']; ?></p>
    <p>You are in user Dashborad page.</p>
    <p><a href="logout.php">logout</a></p>
</div>
    
</body>
</html>