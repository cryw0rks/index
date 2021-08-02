// darkmode feature
var darkMode = false;
function darkModeFunc() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    eraseCookie("theme");
    if (darkMode == true) {
        darkMode = false;
        document.getElementById("darkModeIcon").classList.add('fa-moon');
        document.getElementById("darkModeIcon").classList.remove('fa-sun');
        //document.getElementsByTagName("nav").classList.remove("navbar-dark");
        createCookie("theme", "light", 30000);
    } else {
        darkMode = true;
        document.getElementById("darkModeIcon").classList.add('fa-sun');
        document.getElementById("darkModeIcon").classList.remove('fa-moon');
        //document.getElementsByTagName("nav").classList.add("navbar-dark");
        createCookie("theme", "dark", 30000);
    }
}

function checkTheme() {
    var currentTheme = readCookie('theme');
    if (currentTheme == 'dark') {
        darkMode = true;
    }
}

checkTheme();

//show mobile menu
function showMobileMenu() {
    document.querySelector('.menu-mobile').classList.toggle('clicked');
    document.querySelector('.header-menu').classList.toggle('show');
}