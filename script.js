fetch("http://127.0.0.1:8000/perfil")
.then(response => response.json())
.then(data => {
    document.getElementById("nome").innerText = data.nome
    document.getElementById("idade").innerText = data.idade
    document.getElementById("escolaridade").innerText = data.escolaridade
    document.getElementById("projetos").innerText = data.projetos
})