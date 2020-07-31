$(function() {
    
    $.ajax({
        url: 'http://localhost:5000/listar_livros',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (resposta) {
        for (var i in resposta) {
            lin = '<tr>' +
              '<td>' + resposta[i].nome + '</td>' + 
              '<td>' + resposta[i].autor + '</td>' + 
              '<td>' + resposta[i].ano + '</td>' + 
              '</tr>';
            $('#TabelaSeries').append(lin);
        }
    }

});