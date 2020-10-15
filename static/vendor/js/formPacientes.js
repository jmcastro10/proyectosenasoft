function inicio() {
    $('#ingresarPaciente').submit(function (e) {
        e.preventDefault();
        $.ajax({
            url: 'sendFormPaciente',
            data:$(this).serialize(),
            type: 'post',
            dataType: 'json',
            success: function (respuesta) {
                console.log(respuesta);
            },
            error: function () {
                console.log("No se ha podido obtener la información");
            }
        });
    })

}