<!DOCTYPE html>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
 <link rel="stylesheet" href="/static/css/style.css">

<html>
<body>

<head>

    <title>.File Format Commons</title>

</head>

    <div class="header">
        <a href="/">
                <h1>FFC </h1>
                
        </a>
    
    </div>


   <!--  <div class="header">
        <a href="/">
            <div style="display: inline-block;">
                <img src="/static/images/p_ffc.png" style="margin-left: 34px;">
                <img src="/static/images/f_ffc.png" style="margin-left: 72px;">
                <img src="/static/images/f_ffc.png" style="margin-left: 34px;">
                <img src="/static/images/c_ffc.png" style="margin-left: 34px;">
            </div>
            </a>
            </div> -->



<p id = "demo" ><center>Search for file types and extensions:</center></p>

<form id="myForm">
  <center> <input type="text" id="fname" name="fname">
 <input type="button" id="searchBtn" class="searchBtn" value="Submit"/></center>
</form>







<script>
$(document).bind('keypress', function(e) {
            if(e.keyCode==13){
                e.preventDefault();
                $('#searchBtn').trigger('click');
             }
        });

        $('#searchBtn').click(function(){
            var redirect= "/search/";
            var search_val = $("#fname").val();
            if (search_val !== ""){
                redirect = redirect.concat(search_val,"/");
            }
            else{
                redirect = redirect.concat("%20/");
            }
            console.log(redirect);
            window.location.href = redirect;
             });
</script>
<div style="text-align: left;">
    <a class= "file_title">${name} : </a>
    <ul class= "list_format">
        <li><a class = "file_data">Data Type: ${data} </a></li>
        <li><a class = "file_data">ext: ${ext} </a></li>
        <li><a class = "file_data">Tags: ${tags} </a></li>
        <li><a class = "file_data">File Type: ${file_kind} </a></li><br>
        <li><a class = "file_data" href = "http://en.wikipedia.org/wiki/${wiki}">Wikipedia</a></li><br>
        <li><a class = "file_data" href="/static/download/${download}" download>Download Link</a></li>
    </ul>
</div>



</body>
</html>
