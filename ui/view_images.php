<!DOCTYPE html>
<html>
    <?php 

        $json_file = json_decode("names_and_ratings.json", true);
        foreach($json_file as $json_list){

        }

    ?>
    <head lang="en">
        <meta charset="utf-8">
        <title>RJI Classifier</title>
        <link href="index.css" rel="stylesheet">
    </head> 
    <body>
        <ul>
        <li><a href="/index.php">Search</a></li>
        <li><a href="">About</a></li>
        <li><a href="">Contact</a></li>
        <li><a class="active" href="">View Images</a></li>
        </ul>
        <div id="container">
            <h1>RJI Classifier Ratings</h1>
                <!--<button type="button">View Image Score!</button> -->
            <table id="ratings" border="1">
                <tr>
                    <td id="file_name">Image</td>
                    <td id="tech_rating">Technical Score</td>
                    <td id="aesthetic_rating">Aesthetic Score</td>
                </tr>

                <?php 
                    $json_file = json_decode(file_get_contents("names_and_ratings.json"), true);
                    foreach($json_file as $json_list){ ?>
                    <tr>
                        <td height="119"><?php echo $json_list[0]; ?></td>
                        <td><?php echo $json_list[1]; ?></td>
                        <td><?php echo $json_list[2]; ?></td>
                    </tr>
                <?php } ?>
            </table>
        </div>
    </body>
</html>
