<!DOCTYPE html>
<html lang="en">
    <head>
	<meta charset="utf-8">
	<title>Images and Scores</title>
    </head>
    <body>
	<?php

	    $content = json_decode(file_get_contents("names_and_ratings.json"), true);

	    print_r($content);

	?>
    </body>
</html>
