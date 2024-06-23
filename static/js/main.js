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
console.log(document.querySelectorAll('.tel'))


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
    SizeSlider();
}
window.addEventListener('resize',(e)=>{
    SizeSlider();
});

function SizeSlider () {
    let SizeWindow = document.body.clientWidth;

    if (SizeWindow > 1399) {
        let swiper = new Swiper(".mySwiper", {
            slidesPerView: 3,
            spaceBetween: 41,
            autoplay: {
                delay: 3500,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
        });
    } else {
        let swiper = new Swiper(".mySwiper", {
            slidesPerView: 1,
            spaceBetween: 60,
            autoplay: {
                delay: 1500,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
        });
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
            spaceBetween: 40
        }
    },
    observer: true,
    observeParents: true,
    parallax:true,
});


