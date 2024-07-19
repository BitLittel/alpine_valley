[].forEach.call( document.querySelectorAll('.tel'), function(input) {
    var keyCode;
    function mask(event) {
        event.keyCode && (keyCode = event.keyCode);
        var pos = this.selectionStart;
        if (pos < 3) event.preventDefault();
        var matrix = "+7 (___) ___ ____",
            i = 0,
            def = matrix.replace(/\D/g, ""),
            val = this.value.replace(/\D/g, ""),
            new_value = matrix.replace(/[_\d]/g, function(a) {
                return i < val.length ? val.charAt(i++) || def.charAt(i) : a
            });
        i = new_value.indexOf("_");
        if (i != -1) {
            i < 5 && (i = 3);
            new_value = new_value.slice(0, i)
        }
        var reg = matrix.substr(0, this.value.length).replace(/_+/g,
            function(a) {
                return "\\d{1," + a.length + "}"
            }).replace(/[+()]/g, "\\$&");
        reg = new RegExp("^" + reg + "$");
        if (!reg.test(this.value) || this.value.length < 5 || keyCode > 47 && keyCode < 58) this.value = new_value;
        if (event.type == "blur" && this.value.length < 5)  this.value = ""
    }

    input.addEventListener("input", mask, false);
    input.addEventListener("focus", mask, false);
    input.addEventListener("blur", mask, false);
    input.addEventListener("keydown", mask, false)

});


// POPUP Block VIDEO
function openPopupForm() {
    var PopupForm = document.querySelector('.PopupForm');
    var main = document.querySelector('body');
    var search = document.querySelector(".search--menu");
    search.style.display = "none";
    main.style.overflow = "hidden"
    PopupForm.style.display = 'block';
}
function closePopupForm() {
    var PopupForm = document.querySelector('.PopupForm');
    var main = document.querySelector('body');
    var search = document.querySelector(".search--menu");
    search.style.display = "flex";
    main.style.overflow = "auto";
    PopupForm.style.display = 'none';
}

function OpenFullForm() {
    var FullForm = document.querySelector('.FullForm');
    var main = document.querySelector('body');
    var search = document.querySelector(".search--menu");
    FullForm.style.display = 'block';
    search.style.display = "none";
    main.style.overflow = "hidden"
}
function CloseFullForm() {
    var FullForm = document.querySelector('.FullForm');
    var main = document.querySelector('body');
    var search = document.querySelector(".search--menu");
    search.style.display = "flex";
    main.style.overflow = "auto";
    FullForm.style.display = 'none';
}

// Hamburger__menu
function hamburger__menu() {
    const humberger = document.querySelector(".hamberger__menu"),
        menu = document.querySelector(".search--menu__left"),
        main_selekt = document.querySelector(".main--blok"),
        header_selekt = document.querySelector(".header--conteiner");
    humberger.style.display="block";
    main_selekt.onclick = function (){close__humberger();};
    header_selekt.onclick = function (){close__humberger();};
    menu.onclick = function (){close__humberger();};
}
function close__humberger() {
    const humberger = document.querySelector(".hamberger__menu"),
         menu = document.querySelector(".search--menu__left");
    humberger.style.display="none";
    menu.onclick = function () {hamburger__menu();};
}

// opisanie-button

function showDiscript(){
    const around = document.querySelector(".conteiner--3__content");
    around.style.display="none";
    const discription = document.querySelector(".conteiner--3__content--discript");
    discription.style.display="flex";

    const but3 = document.querySelector(".button_3");
    but3.style.color ="#FFF4DE";
    but3.style.background ="#395340";

    const but4 = document.querySelector(".button_4");
    but4.style.color ="#395340";
    but4.style.background ="#FFF4DE";


}
function showAroundr(){
    const around = document.querySelector(".conteiner--3__content");
    around.style.display="flex";
    const description = document.querySelector(".conteiner--3__content--discript");
    description.style.display="none";

    const but4 = document.querySelector(".button_4");
    but4.style.color ="#FFF4DE";
    but4.style.background ="#395340";

    const but3 = document.querySelector(".button_3");
    but3.style.color ="#395340";
    but3.style.background ="#FFF4DE";


}


window.onload = function (){
    CloseHamberger();
    newSwiper_positionArrow();
    mySwiper_positionArrow_2();
}
window.addEventListener('resize',(e)=>{
    CloseHamberger();
    newSwiper_positionArrow();
    mySwiper_positionArrow_2();
});

function CloseHamberger () {
    let SizeWindow = document.body.clientWidth;
    if (SizeWindow > 1399){
        const CloseHamberger = document.querySelector(".close__hambirger")
        CloseHamberger.style.display="none";
    }
}

function open_popup(img) {
    let popup = document.getElementById('popup'),
        popup_img = document.getElementById('popup_img');
    popup.style.display = 'block';
    popup_img.src = img;
}

let swiper_slide = document.querySelectorAll('.swiper-slide__img');
for (let i = 0; i < swiper_slide.length; i++) {
    swiper_slide[i].onclick = function () {
        open_popup(swiper_slide[i].src);
    };
}

var swiper = new Swiper(".NewSwiper", {
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    direction: 'horizontal',
    loop: true,
    slidesPerView: 1,
    watchOverflow: true,
    spaceBetween: 60,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    autoplay: {
        delay: 1500,
    },
    breakpoints: {
        640: {
            slidesPerView: 1,
            spaceBetween: 60
        }
    }
});

var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 60,
    autoplay: {
        delay: 1500,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        1399:{
            slidesPerView: 3,
            spaceBetween: 45,
            autoplay: {
                delay: 3500,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
        }
    }
});

function newSwiper_positionArrow() {
    let NewSwiper = document.getElementById('NewSwiper'),
        new_swiper_next = document.getElementById('new_swiper_next'),
        new_swiper_prev = document.getElementById('new_swiper_prev');

    let offset_top_new_swiper = NewSwiper.offsetTop,
        client_height_new_swiper = NewSwiper.clientHeight/2,
        client_width_new_swiper = NewSwiper.clientWidth,
        offset_left_new_swiper = NewSwiper.offsetLeft,
        client_width_new_swiper_next = new_swiper_next.clientWidth;

    new_swiper_next.style.top = offset_top_new_swiper + client_height_new_swiper + 'px';
    new_swiper_prev.style.top = offset_top_new_swiper + client_height_new_swiper + 'px';
    new_swiper_next.style.left = client_width_new_swiper + offset_left_new_swiper - client_width_new_swiper_next + 20 + 'px';
    new_swiper_prev.style.left = offset_left_new_swiper - 20 + 'px';

}


function mySwiper_positionArrow_2() {
    let mySwiper = document.getElementById('mySwiper'),
        New_swiper_next1 = document.getElementById('New_swiper_next1'),
        New_swiper_prev1 = document.getElementById('New_swiper_prev1');

    let top_my_swiper = mySwiper.offsetTop,
        client_height_my_swiper = mySwiper.clientHeight/2,
        client_width_my_swiper = mySwiper.clientWidth,
        left_my_swiper = mySwiper.offsetLeft,
        client_width_my_swiper_next = New_swiper_next1.clientWidth;

    New_swiper_next1.style.top = top_my_swiper + client_height_my_swiper - 20 + "px";
    New_swiper_prev1.style.top = top_my_swiper + client_height_my_swiper - 20 + "px";
    New_swiper_next1.style.left = client_width_my_swiper + left_my_swiper - client_width_my_swiper_next - 10 + "px";
    New_swiper_prev1.style.left = left_my_swiper + 10 + "px";
}


const GetForm = document.getElementById("form_1");
GetForm.addEventListener("submit", saveArticle);
function saveArticle(event) {
    event.preventDefault();

    const FormData_1 = new FormData(GetForm);
    const FormData_1_AS_Object = Object.fromEntries(FormData_1);

    console.log(FormData_1_AS_Object);
}
