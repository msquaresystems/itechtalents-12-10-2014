$(document).ready(function()
{
  $("p.followbtns .btn-success").text("UnFollow");	

  $(".follow").click(function(){
    var tid=$(this).attr("id");
    var params ={param1:tid};             
     $.ajax({ url: "/quorum/topic/follow/",
              dataType: "json",
              data: params,           
              success: setResult      
      });  
    if ($(this).hasClass("btn-inverse")){
        $(this).removeClass("btn-inverse");
        $(this).addClass("btn-success"); 
        $(this).text("UnFollow");
     }else{
        $(this).removeClass("btn-success");
        $(this).addClass("btn-inverse"); 
        $(this).text("Follow");
    }       
  });
 
  function setResult(data) {
    // data.updated=(followed,unfollowed, nouser) 
    if (data.updated=="nouser"){
      alert(data.updated);   
    }            
  }
});