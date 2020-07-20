let hamburgerButton = document.querySelector('.hamburger-menu');
let lateralMenu = document.querySelector('.sidebar');
let overlay = document.querySelector('.overlay');

const transformState = () => {
    hamburgerButton.classList.toggle('opened');
    lateralMenu.classList.toggle('opened');
    overlay.classList.toggle('opened');
};

hamburgerButton.addEventListener('click', transformState);
overlay.addEventListener('click', transformState);
