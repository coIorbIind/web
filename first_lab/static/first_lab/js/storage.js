// localStorage.language = "RU";

const button = document.getElementById("lang");
let menu_items = document.getElementsByClassName("menu__item")

// console.log(temp_menu)

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

// button.innerText = getCookie("language");
console.log(document.cookie);

const menu = {
    about_us: "О нас-About Us",
    register: "Регистрация-Registration",
    authorize: "Авторизоваться-Authorize",
    logout: "Выйти-Log Out"
}

// const ru_menu = ["О нас", "Регистрация", "Авторизоваться", "Выйти"]
// const en_menu = ["About Us", "Registration", "Authorize", "Log Out"]

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

// function changeMenu(language) {
//     if (language === "RU"){
//         if (menu_items[2].innerText === "Log Out"){
//                 menu_items[2].innerText = ru_menu[ru_menu.length - 1]
//             }
//             else {
//                 menu_items[2].innerText = ru_menu[ru_menu.length - 2]
//             }
//     }
//     else{
//         if (menu_items[2].innerText === "Выйти"){
//                 menu_items[2].innerText = en_menu[en_menu.length - 1]
//             }
//             else {
//                 menu_items[2].innerText = en_menu[en_menu.length - 2]
//             }
//     }
//     // for (let menuItemKey = 0; menuItemKey < ru_menu.length - 2; menuItemKey++) {
//     //
//     // }
//
//     for (let menuItemKey = 0; menuItemKey < ru_menu.length - 2; menuItemKey++) {
//         if (language === "RU"){
//             menu_items[menuItemKey].innerText = ru_menu[menuItemKey]
//         }
//         else{
//             menu_items[menuItemKey].innerText = en_menu[menuItemKey]
//         }
//     }
// }
// location.reload();
button.addEventListener('click', onClick);
