document.addEventListener('keydown', function(event) {
    if (event.key === 'F2') {
        pagModal(event);
    } else if (event.key === 'F3') {
        mostrarModal(event);
    } else if (event.key === 'F4') {
        printVenda();
    } else if (event.key === 'F6') {
        printComanda();
    }
});

// script2.js
function mostrarModal() {
    event.preventDefault();
    $("#item-id").select2();
    document.getElementById('meuModal').style.display = 'block';
    $("#item-id").select2('open');
    document.addEventListener('keydown', fecharComEsc);
}

function fecharModal() {
    document.removeEventListener('keydown', fecharComEsc);
    $("#item-id").select2('close');
    document.getElementById('meuModal').style.display = 'none';
}

// script3.js
$(document).ready(function () {
    $("#item-id").on('select2:close', function (e) {
        $('#texto').focus().select();
    });
});

// script4.js
function formatWord(word) {
    if (word.length > 15) {
        return word.slice(0, 15); // Truncate para os primeiros 10 caracteres
    } else {
        const padding = ' '.repeat(15 - word.length); // Calcula o número de espaços de preenchimento
        return word + padding; // Adiciona o preenchimento à palavra
    }
}

// script6.js
function pagModal() {
    event.preventDefault();
    document.getElementById('pagModal').style.display = 'block';
    document.getElementById('text_quant').focus();
    document.getElementById('text_quant').select();
    document.addEventListener('keydown', fecharComEsc);
}

function fecharComEsc(event) {
    if (event.keyCode === 27) {
        fecharModal();
        pagfecharModal();
    }
}

function pagfecharModal() {
    event.preventDefault();
    document.removeEventListener('keydown', fecharComEsc);
    document.getElementById('pagModal').style.display = 'none';
}
