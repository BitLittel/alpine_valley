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
    var PopupForm = document.querySelector('.PopupForm'),
        main = document.querySelector('body');
    PopupForm.style.display = 'block';
    main.style.overflow = "hidden"
}
function closePopupForm() {
    var PopupForm = document.querySelector('.PopupForm'),
        main = document.querySelector('body')
    main.style.overflow = "auto";
    PopupForm.style.display = 'none';
}

// Hamburger__menu
function hamburger__menu() {
    const humberger = document.querySelector(".hamberger__menu"),
        menu = document.querySelector(".search--menu__left");
    humberger.style.display="block";
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
    const around = document.querySelector(".conteiner--3__content")
    around.style.display="none";
    const discription = document.querySelector(".conteiner--3__content--discript")
    discription.style.display="flex";
}

function showAroundr(){
    const around = document.querySelector(".conteiner--3__content")
    around.style.display="flex";
    const description = document.querySelector(".conteiner--3__content--discript")
    description.style.display="none";
}


var swiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 41,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});