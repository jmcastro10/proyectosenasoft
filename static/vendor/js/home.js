function inicio() {
    $('#cliente').submit(function (e) {
        e.preventDefault();
        $.ajax({
            url: 'sendjson/',
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