// console.log(navigator.language.split("-")[1])

const button = document.getElementById("lang");
let menu_items = document.getElementsByClassName("menu__item")


function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

console.log(document.cookie);

const menu = {
    about_us: "О нас-About Us",
    register: "Регистрация-Registration",
    authorize: "Авторизоваться-Authorize",
    logout: "Выйти-Log Out"
}


function onClick() {
    let text = button.textContent;
    if (text === "RU"){
        // changeMenu("EN")
        button.innerText = "EN";
        localStorage.language = "EN";
        document.cookie = "language=EN; path=/;";

    }
    if (text === "EN"){
        // changeMenu("RU")
        button.innerText = "RU";
        localStorage.language = "RU";
        document.cookie = "language=RU; path=/;";
    }
    location.reload();
    console.log(document.cookie);
}

button.addEventListener('click', onClick);
