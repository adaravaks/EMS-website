window.onscroll = function() {buttonDisplayFunction()};

function buttonDisplayFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("scroll-top-button").style.opacity = "1";
        document.getElementById("scroll-top-button").style.cursor = "pointer";
    } else {
        document.getElementById("scroll-top-button").style.opacity = "0";
        document.getElementById("scroll-top-button").style.cursor = "default";
    }
}

function scrollTopFunction() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}