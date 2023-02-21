<?php
session_start();
    $dbhost = "localhost";
    $dbuser = "root";
    $dbpass = "";
    $dbname = "login";
    if(!$con = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname))
    {
        die("failed to connect!");
    }


    if($_SERVER['REQUEST_METHOD'] == "POST")
    {
        $username = $_POST['username'];
        $password = $_POST['password'];
        $confirm_password = $_POST['confirm_password'];
        $First_Name = $_POST['first_Name'];
        $Last_Name = $_POST['last_Name'];


        if(empty($username) && empty($password) && empty($confirm_password) && empty($First_Name) && empty($Last_Name))
        {
            echo "Please enter valid information";


        }elseif($password != $confirm_password)
        {
            echo "Passwords have to match";
        }else
        {
            $query = "insert into login (username,password,confirm_password,First_Name,Last_Name) values ('$username','$password','$confirm_password','$First_Name','$Last_Name')";
            mysqli_query($con, $query);
            header("location: login.php");
            die;
        }   
    }


?>



<!DOCTYPE html>
<html>
<head>
    <title>Registration Page</title>
    <link rel="stylesheet" href="css/register.css"/>
</head>
<body>
    <section class="main">
        <div class="Register">
        <h1>Register Now</h1>
        <form method='post'>
            <input type="text" name="First_Name" placeholder="Enter your First Name"/>
            <input type="text" name="Last_Name" placeholder="Enter your Second Name"/>
            <input type="text" name="username" placeholder="Enter a Username"/>
            <input type="password" name="password" placeholder="Enter your Password"/>
            <input type="password" name="confirm_password" placeholder="Confirm your Password"/>
            <button class="Submit-button">Submit</button>
        </form>
        </div>
    </section>
</body>
</html>