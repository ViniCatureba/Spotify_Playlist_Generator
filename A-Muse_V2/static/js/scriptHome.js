function goToHome(){
    window.location.href = "/"
}
function goToCreatePlaylist(){
    window.location.href = "/createPlaylist"
}
function goToAboutUs(){
    window.location.href = "/aboutus"
}
function goToFAQ(){
    window.location.href = "/faq"
}

function logado(){
    window.alert("Logando...")
}

function logoff(){
    window.alert("Deslogado com sucesso! Também acesse 'https://www.spotify.com/br-pt/account/apps/' e faça seu logoff no site do spotify!")
    window.open('https://www.spotify.com/br-pt/account/apps/','__blank')
}

hamburger = document.querySelector(".hamburger");
nav = document.querySelector("nav");
hamburger.onclick = function() {
        nav.classList.toggle("active");
}


