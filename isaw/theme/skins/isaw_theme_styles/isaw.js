jq(document).ready(function(){
   // apply a class to nav elements to keep hover styles when on submenu
   jq("li .submenu").hover(
     function () { jq(this).parent().addClass("hover"); }, 
     function () { jq(this).parent().removeClass("hover"); }
   );
   
   // move page elements down for longer titles
   var titleHeight = jq("#above-content").height();
   jq("#content, #edit-bar").css("margin-top",titleHeight + 9);
   jq("#portal-column-two .visualPadding").css("margin-top",titleHeight + 1);
   jq("#socialtools").css("padding-top",titleHeight - 44);
   
});


jq(window).load(function(){
    // set width on image <dl>s to be set at the width of the image
    // to keep caption from pushing out the width
    capnum = jq("dl.captioned").length;

    for(i = 0; i < capnum; i++) {
         imgWidth = jq("dl.captioned img").eq(i).width();
         jq("dl.captioned").css("width",imgWidth);
    }
    
    // align faculty e-mail/info link to bottom of image if text isn't too tall
    for(i = 0; i < jq(".facultyListing").length; i++) {
       var imageHeight = jq(".facultyListing img").eq(i).height() + 12;
       var descripHeight = jq(".facultyInfo").eq(i).height();
       if (descripHeight > imageHeight) {
           jq(".facultyListing .alignBottom").eq(i).css("position","relative");
       }
    }
});