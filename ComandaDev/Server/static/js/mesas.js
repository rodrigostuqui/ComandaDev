// Script para lidar com eventos de teclado
document.addEventListener('keydown', function(event) {
    if (event.key === 'F2') {
        document.getElementById('form1').submit();
    } else if (event.key === 'F3') {
        mostrarModal(event);
    }
});

// Script para atualizar a lista de mesas usando WebSockets
$(document).ready(function () {
    var ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
    var ws_path = ws_scheme + '://' + window.location.host + "/ws/mesa_atualizacao/";
    var websocket = new WebSocket(ws_path);

    websocket.onmessage = function (event) {
        var data = JSON.parse(event.data);
        updateMesaList(data.mesas);
    };
});
function updateMesaList(data) {
    var mesaList = $('#mesa-list');
    mesaList.empty();

    if (Array.isArray(data)) {
        data.forEach(function (mesa) {
            var mesaItem = '<a href="/itensmesa/?mesa_id=' + mesa.mesa + '"><button id="mesa" class="btn btn-dark" name="mesa_id" value="' + mesa.mesa + '">' + mesa.mesa + '</button></a>';
            mesaList.append(mesaItem);
        });
    } else {
        console.error("Dados recebidos não são um array:", data);
    }
}

// Funções para lidar com a exibição do modal
function mostrarModal(event) {
    event.preventDefault();
    document.getElementById('meuModal').style.display = 'block';
    document.getElementById('texto').focus();
    document.addEventListener('keydown', fecharComEsc);
}

function fecharComEsc(event) {
    if (event.keyCode === 27) { // Código da tecla "Esc"
        fecharModal();
    }
}

function fecharModal() {
    document.removeEventListener('keydown', fecharComEsc);
    document.getElementById('meuModal').style.display = 'none';
}