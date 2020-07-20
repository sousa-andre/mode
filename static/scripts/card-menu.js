let cardIcons = document.querySelectorAll('.card-menu-icon');

cardIcons.forEach(cardIcon => cardIcon.addEventListener('click', ()=>{
    let cardMenu = cardIcon.parentElement;
    let cardMenuDropdown = cardMenu.querySelector('.card-menu-dropdown')
    if (cardMenuDropdown.style.display === 'flex') {
        cardMenuDropdown.style.display = 'none';
    } else {
        cardMenuDropdown.style.display = 'flex';
    }
}));
cardIcons.forEach(cardIcon => {
    let cardMenu = cardIcon.parentElement;
    let cardMenuDropdown = cardMenu.querySelector('.card-menu-dropdown')
    if (!cardMenuDropdown.querySelector('a')) {
        cardMenu.style.display = 'none';
    }
})

