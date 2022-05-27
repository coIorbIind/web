// console.log(navigator.language.split("-")[1])

const button = document.getElementById("lang");
const html_ = document.querySelector('html');

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
        html_.setAttribute('lang', 'en');
    }
    if (text === "EN"){
        // changeMenu("RU")
        button.innerText = "RU";
        localStorage.language = "RU";
        document.cookie = "language=RU; path=/;";
        html_.setAttribute('lang', 'ru');
    }
    location.reload();
    console.log(document.cookie);
}

button.addEventListener('click', onClick);
