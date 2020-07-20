let notificationDiv = document.querySelector('#notification');
let notificationIcon = notificationDiv.querySelector('.notification-icon')
let notificationDropDown = notificationDiv.querySelector('.notification-dropdown')

notificationIcon.addEventListener('click', ()=>{
    if (notificationDropDown.style.display === 'flex') {
        notificationDropDown.style.display = 'none';
    } else {
        notificationDropDown.style.display = 'flex';
    }
});
