<?php
$YourName = isset($_REQUEST['Your_Name']) ? $_REQUEST['Your_Name'] : '';
$FavoriteWord = isset($_REQUEST['Favorite_Word']) ? $_REQUEST['Favorite_Word'] : '';
?>
<html>
<head>
<title>Form-Message Passing</title>
</head>
<body bgcolor="#FFFFFF" text="#000000">
<p>Hai <?php echo $YourName; ?></p>
<p>You like the word <b><?php echo $FavoriteWord; ?></b>?</p>
</body>
</html>
