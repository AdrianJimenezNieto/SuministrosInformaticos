
window.addEventListener('load', function () {
    const msg = document.getElementsByName('message');

    setTimeout( function () {
        msg.forEach(element => element.classList.add('animation-message'));
    }, 1);

    setTimeout( function () {
        msg.forEach(element => element.classList.remove('animation-message'));
    }, 2000);

    setTimeout( function () {
        msg.forEach(element => element.classList.remove('hide-message'));
    }, 2750);

})
