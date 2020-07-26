let menu = document.getElementsByClassName("navbar");
// menu.addEventListener("scroll",function(){
//     console.log("done");

// });
let ycord = window.pageYOffset;
window.addEventListener('scroll', function() 
    {//console.log('scrolling');
    let ycord2 = window.pageYOffset;
    if (ycord < ycord2)
    {
        console.log("pagedown");
        for(var i = 0; i < menu.length; i++){
          menu[i].style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
             }
        
    }
    else if ( ycord2 == 0)
    {
        console.log("noscroll");
        for(var i = 0; i < menu.length; i++){
            menu[i].style.background = 'transparent';
            menu[i].style.border = '0px';
            menu[i].style.color = "#000000"; 
               }
    
    }    
    else
    {
        console.log("pageup");
        
    

    }
    ycord = ycord2;
});