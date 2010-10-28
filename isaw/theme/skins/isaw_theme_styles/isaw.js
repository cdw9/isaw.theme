jq(document).ready(function(){
   // apply a class to nav elements to keep hover styles when on submenu
   jq("li .submenu").hover(
     function () { jq(this).parent().addClass("hover"); }, 
     function () { jq(this).parent().removeClass("hover"); }
   );   
});


jq(window).load(function(){
    // set with on image <dl>s to be set at the width of the image
    // if there is a caption, the width gets pushed out
    capnum = jq("dl.captioned").length;
    console.log(capnum);

    for(i = 0; i < capnum; i++) {
         imgWidth = jq("dl.captioned img").eq(i).width();
         jq("dl.captioned").css("width",imgWidth);
    }
});