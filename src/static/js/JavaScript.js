
function redirecRegistro() {
    window.location.href = "{{ url_for('registro') }}";
}

function redirecLogin() {
    window.location.href = "{{ url_for('login') }}";
}

function redirecInicio() {
    window.location.href = "{{ url_for('') }}";
}