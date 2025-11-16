async function carregarVendas() {
    const produto = document.getElementById("buscar-produto").value;
    const canal = document.getElementById("buscar-canal").value;

    const url = new URL("http://localhost:8000/api/vendas");

    if (produto) url.searchParams.append("produto", produto);
    if (canal) url.searchParams.append("canal", canal);

    const resposta = await fetch(url);
    const dados = await resposta.json();

    const tabela = document.getElementById("tabela-vendas");
    tabela.innerHTML = "";

    dados.forEach(v => {
        tabela.innerHTML += `
            <tr>
                <td>${v.produto}</td>
                <td>${v.quantidade}</td>
                <td>${v.canal}</td>
                <td>${v.data_venda}</td>
                <td>R$ ${v.valor_total}</td>
            </tr>
        `;
    });
}

carregarVendas();