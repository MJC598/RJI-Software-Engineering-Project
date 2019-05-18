<!DOCTYPE html>
<html>
	<head lang="en">
		<meta charset="utf-8">
		<title>RJI Classifier</title>
		<link href="index.css" rel="stylesheet">
        <script src="index.js"></script>
        
	</head>	
	<body>
	    <ul id= "navbar">
		<li><a href="index.php">Search</a></li>
		<li><a href="">About</a></li>
		<li><a href="">Contact</a></li>
        <li><a class="active" href="">Upload</a></li>
		<li><a href="/view_images.php">View Images</a></li>
	    </ul>
	    <div id="container">
		<h1>Image Upload</h1>
            
             <div class="input-container">
            <input type="file" id="real-input">
                <button id="browse-btn">
                    Choose File
                 </button>
            <span id="file-info"></span>
            </div>
        </div>
        
        <script type="text/javascript">
        
        
        const realInput = document.getElementById("real-input");
        const browseBtn = document.getElementById("browse-btn");
        const fileInfo = document.getElementById("file-info");

        browseBtn.addEventListener("click", function() {
   
        realInput.click();
    
        });
        
    /*    realInput.addEventListener("change", function(){
            if (realInput.value){
        customTxt.innerHTML = realInput.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
    } else {
        customTxt.innerHTML = "No file chosen.";
    }
    
}); */
        
        
        </script>
        
	</body>
</html>
