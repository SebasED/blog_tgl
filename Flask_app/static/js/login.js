var formLogin = document.getElementById('login');

formLogin.onsubmit = function(event){
    event.preventDefault();

    var formulario = new FormData(formLogin);

    fetch('/session_start', {method: 'POST', body: formulario})
        .then(Response => Response.json())
        .then(data=>{
            if (data.message=="validated"){
                window.location.href = "/welcome"
            }

            var mensajeAlerta = document.getElementById('mensajeLogin');
            mensajeAlerta.innerHTML = data.message;
            mensajeAlerta.classList.add("alert");
            mensajeAlerta.classList.add("alert-danger");

        });
}