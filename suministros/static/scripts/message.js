console.log('lo tengo')

window.addEventListener('load', function () {
    const msg = document.getElementById('user-message');

    setTimeout( function () {
        msg.classList.add('animation-message');
    }, 1);

    setTimeout( function () {
        msg.classList.remove('animation-message');
    }, 2000);

    setTimeout( function () {
        msg.classList.add('hideMessage');
    }, 2750);

})
