<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <?php 
    require('db.php');
    session_start();

    if(isset($_POST['username'])) {
        $username = stripslashes($_REQUEST['username']);
        $username = mysqli_real_escape_string($con, $username);
        $password = stripslashes($_REQUEST['password']);
        $password = mysqli_real_escape_string($con, $password);
        $query = "SELECT * FROM `users` WHERE username = '$username' AND password = '".md5($password)."'";
        $result = mysqli_query($con, $query) or die(mysqli_error($con));
        $rows = mysqli_num_rows($result);
        if($rows == 1) {
            $_SESSION['username'] = $username;
            header("Location: dashboard.php"); 
        } else {
            echo "<div class='form'> 
            <h3> Incorrect username and password </h3> <br/>
            <p class='link'> Click here to <a href='login.php'> Login</a> again </p>
            </div>";
        }
    } else {
    ?>
    <form class="form" method="post" name="login">
        <h1 class="login-title">Login</h1>
        <input type="text" class="login-input" name="username" placeholder="Username" autofocus="true"/>
        <input type="password" class="login-input" name="password" placeholder="Password"/>
        <input type="submit" value="Login" name="submit" class="login-button"/>
        <p class="link">Don't have an account? <a href="registration.php">Registration Now</a></p>
    </form>
    <?php } ?>
</body>
</html>
