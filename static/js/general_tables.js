function startUp() {
    document.querySelector('#id_code').setAttribute('disabled', '');
}
document.addEventListener("DOMContentLoaded", startUp);

select_btn = document.querySelectorAll('.select-pref');

select_btn.forEach(btn => btn.addEventListener('click', function (e) {
    e.preventDefault()
    btn_code = e.target.dataset.code
    document.getElementById('clicked-code').value = btn_code
    select_btn = document.querySelector('#select-pref-btn').click();
}));


