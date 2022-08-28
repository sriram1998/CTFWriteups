<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trial by PHP</title>

    <!-- With assets by Jorge Avila. Let the war on robots continue to the end of time!-->

    <style>
        * {
            box-sizing: border-box;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
        }

        body {
            box-shadow: 0 0 3px #ccc;
            cursor: url('/assets/cursor.png'), auto;
            background: url('/assets/stone.png') no-repeat;
            background-size: cover;
            background-color: #312b29;
            box-shadow: 5px 10px;
            font-family: Garamond, "Times New Roman";
            margin: 0;
            min-height: 100vh;
            padding: 32px;
            border: 6px ridge #38312a;
        }

        main {
            background: url('/assets/background.png') no-repeat;
            background-size: cover;
            width: 490px;
            height: 738px;
            display: block;
            padding: 64px;
            margin: 0 auto;
            filter: drop-shadow(16px 16px 32px #111);
        }

        h1 {
            color: darkblue;
        }
        
        li {
            color: yellow;
        }

        .success {
            color: green;
        }

        .fail {
            color: red;
        }

        #flag {
            font-family: fantasy, cursive;
            transform: rotate(-25deg);
            overflow-wrap: break-word;
            font-weight: bold;
            opacity: 0.25;
            color: brown;
            font-size: 32px;
        }
    </style>
</head>
<body>
    <?php
        $egg = (hash_hmac("md5", $_COOKIE["egg"], "DEADLYDRAGON") == 0);

        $deep = isset($_GET["deep"]) && (strlen(base64_encode(abs($_GET["deep"]))) < strlen($_GET["deep"]));

        $hedge = isset($_GET["THROUGH_A_TRAP_LADEN_MAZE"]) && (strpos(urldecode($_SERVER['QUERY_STRING']), "_") === false);
    ?>

    <main>
        <h1>Trial by PHP</h1>
        <i>Complete 3 impossible tasks to prove that you're a real PHP wizard, Harry.</i>

        <ol>
            <li class="<?php echo $egg ? 'success' : 'fail'; ?>">Produce a hash that's unusually small.</li>

            <li class="<?php echo $deep ? 'success' : 'fail'; ?>">Provide an input that gets shorter with encoding.</li>
            
            <li class="<?php echo $hedge ? 'success' : 'fail'; ?>">Recite the passphrase, without speaking the character who shall not be named.</li>
        </ol>

        <p id="flag"><?php if ($egg && $deep && $hedge) { include("flag.inc.php"); echo $FLAG; } ?></p>
    </main>
</body>
</html>