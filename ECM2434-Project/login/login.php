<!DOCTYPE html>
<html lang = "en">
    <?php session_start(); ?>

<head>
    <title> login Page </title>
</head>
<body>
    <section class="main">
        <div class="main-heading">
            <?php if(!isset($_SESSION["username"])) { ?>
                <section class=login-register>
                    <div class=login-details>
                        <h1>Enter your Login</h1>
                    </div>
                    <form>
                        <input type=text name=username placeholder='Enter your Username'/>
                        <input type=password name=password placeholder='Enter your password'/>
                        <button class=login-button>Login</button>
                    </form>
                    <div class=register>
                        Don't have a user account?, <a href=register.php name=register>Register now</a>
                    </div>
                </section>       
                <?php
                    $dbhost = "localhost";
                    $dbuser = "root";
                    $dbpass = "";
                    $dbname = "login";
                    $error = false;
                    if(!$con = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname)){
                        $error = true;
                    }
                    $username = $_GET['username'];
                    $password = $_GET['password'];
            
            
                    if(empty($username) || empty($password)){
                        $error = true;
                    }
                    $query = "select username from login where username ='$username' and password='$password'";
                    $result = mysqli_query($con, $query);
                    if($result && mysqli_num_rows($result) == 0){
                        $error = true;
                    }
                    mysqli_close($con);
                    if(!$error){
                        $_SESSION["username"] = $username;
                        header("Location: login.php");
                        
                    }

                ?>
            <?php } ?>
            <?php if(isset($_SESSION["username"])){ ?>
                <h1>You Have Succesfully logged in!</h1>
                <a href=logout.php class='logout'>Logout</a> 
            <?php } ?>
            
        </div>
    </section>
</body>
</html>