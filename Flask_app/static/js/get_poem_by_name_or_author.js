var form = document.getElementById('welcome');

form.onsubmit = function(event){
    event.preventDefault();

    var formulario = new FormData(form);
    fetch('/get_poem_by_user', {method: 'POST', body: formulario})
        .then(Response => Response.json())
        .then(data=>{
            if (data.message=="validated"){
                window.location.href = "welcome.html"
            }
            var mensajeAlerta = document.getElementById('alert');
            mensajeAlerta.innerHTML = data.message;
            mensajeAlerta.classList.add("alert");
            mensajeAlerta.classList.add("alert-danger");

        });
}