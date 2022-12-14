var formActualizar = document.getElementById('formActualizar');

formActualizar.onsubmit = function(event){
    event.preventDefault();

    var formulario = new FormData(formActualizar);
    fetch('/modificar_poema', {method: 'POST', body: formulario})
        .then(Response => Response.json())
        .then(data=>{
            if (data.message=="validated"){
                
                window.location.href = "/welcome"
            }

            var mensajeAlerta = document.getElementById('mensajeAlerta');
            mensajeAlerta.innerHTML = data.message;
            mensajeAlerta.classList.add("alert");
            mensajeAlerta.classList.add("alert-danger");

        });
}
