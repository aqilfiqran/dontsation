const navItems = document.querySelectorAll('.nav-item');
let pathname = window.location.pathname;

navItems.forEach(item => {
    if (item.getAttribute('data-link') === pathname)
        item.classList.add('active')
    else
        item.classList.remove('active')
})