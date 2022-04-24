const checkBox = document.getElementById('myCheckBox');
const p = document.getElementById("p1");
const img = document.getElementById("like_icon");

async function onChange () {
    let array = window.location.href.split("/");
    let pk = array[array.length - 1];
    console.log(pk);
    let data = {recipe_id: pk};
    let url = "http://127.0.0.1:8000/api/v1/set_like/";
    let response;

    if (checkBox.checked){

         response = await fetch(url, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
                "X-CSRFToken": document.cookie.split("=")[1]
            },
        })
        if (response.ok){
            changeLikeIcon(true);
        }
    }
    else {
        response = await fetch(url, {
            method: 'DELETE',
            credentials: 'include',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
                "X-CSRFToken": document.cookie.split("=")[1]
            },
        });
        if (response.ok){
            changeLikeIcon(false);
        }
    }
    if (response.ok){
        await changeLikesCount(url, pk);
    }
    else {
        let error_data = await response.json();
        alert(error_data["error"]);
    }
}

// function getUrlVars() {
//     // console.log(window.location.href.split("/")[array.length - 1]);
//     let vars = {};
//     let parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
//     vars[key] = value;
//     });
//     return vars;
// }

async function changeLikesCount(url, pk) {
    let new_url = url + "?pk=" + pk;
    let likes = await fetch(new_url, {
        method: 'GET',
        credentials: 'include',
    })
    if (likes.ok){
        let json_data = await likes.json();
        p.innerText = json_data["likes_count"];
    }
    else {
        let error_data = await likes.json();
        alert(error_data["error"]);
    }
}

function changeLikeIcon(flag) {
    if (flag){
        img.src = "../media/icons/Group 26.png"
    }
    else {
        img.src = "../media/icons/Group 25.png"
    }
}



checkBox.addEventListener('change', onChange);
