function goToHome(){
    window.location.href = "home.html"
}
function goToCreatePlaylist(){
    window.location.href = "createPlaylist.html"
}
function goToAboutUs(){
    window.location.href = "aboutUs.html"
}
hamburger = document.querySelector(".hamburger");
nav = document.querySelector("nav");
hamburger.onclick = function() {
        nav.classList.toggle("active");
}
