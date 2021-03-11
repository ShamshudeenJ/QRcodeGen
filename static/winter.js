
function msg(){
 
         var a=document.getElementById("upload").value;
        
         var xmlhttp=new XMLHttpRequest();
         var url="http://127.0.0.1:5002/api/v1/resources/qrimage?id="+a;
         xmlhttp.open("GET",url,true);
         xmlhttp.send();

         xmlhttp.onreadystatechange=function(){
             var myarr=JSON.parse(this.responseText);
             var ab=myarr.slice(2,-1);
             document.getElementById('image').src = "data:image/png;base64,"+ab;
         }
         document.getElementById("upload").value='';

}
  
  
