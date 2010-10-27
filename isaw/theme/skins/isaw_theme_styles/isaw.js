jq(document).ready(function(){
   // apply a class to nav elements to keep hover styles when on submenu
   jq("li .submenu").hover(
     function () { jq(this).parent().addClass("hover"); }, 
     function () { jq(this).parent().removeClass("hover"); }
   );
   
});