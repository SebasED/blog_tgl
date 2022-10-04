var formActualizar = document.getElementById('formActualizar');

formActualizar.onsubmit = function(event){
    event.preventDefault();

    var formulario = new FormData(formActualizar);
    print('---------------')
    print(formulario)
    fetch('/modificar_poema', {method: 'POST', body: formulario})
        .then(Response => Response.json())
        .then(data=>{
            if (data.message=="validado"){
                
                window.location.href = "/bienvenido"
            }

            var mensajeAlerta = document.getElementById('mensajeAlerta');
            mensajeAlerta.innerHTML = data.message;
            mensajeAlerta.classList.add("alert");
            mensajeAlerta.classList.add("alert-danger");

        });
}
