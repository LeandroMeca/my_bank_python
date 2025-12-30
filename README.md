<h1>🏦 Sistema Bancário em Python</h1>

<img src="https://img.shields.io/badge/Python-3-blue">
<img src="https://img.shields.io/badge/Status-Concluído-brightgreen">
<img src="https://img.shields.io/badge/Projeto-Educacional-yellow">
<img src="https://img.shields.io/badge/Terminal-CLI-lightgrey">

<h2>📌 Descrição Geral</h2>
<ul>
    <li>💻 Sistema bancário simples desenvolvido em Python</li>
    <li>🖥️ Executado em ambiente de terminal</li>
    <li>🏦 Simula operações bancárias reais com regras e limites</li>
</ul>

<h2>📋 Menu do Sistema</h2>
<ul>
    <li>💰 [d] Depositar</li>
    <li>💸 [s] Sacar</li>
    <li>📄 [e] Extrato</li>
    <li>🚪 [q] Sair</li>
</ul>

<h2>🔄 Transações Bancárias</h2>

<h3>💰 Depósito</h3>
<ul>
    <li>O usuário informa um valor para adicionar ao saldo da conta</li>
    <li>Somente valores maiores que zero são aceitos</li>
    <li>Quando o saldo está negativo, é aplicada uma taxa de 1% sobre a dívida</li>
    <li>O usuário pode confirmar ou cancelar o depósito após ver a taxa</li>
    <li>O valor do depósito é reduzido pela taxa aplicada</li>
    <li>Todas as operações são registradas no extrato</li>
</ul>

<h3>💸 Saque</h3>
<ul>
    <li>O usuário informa o valor desejado para saque</li>
    <li>Limite máximo de R$ 500,00 por saque</li>
    <li>Máximo de 3 saques por execução</li>
    <li>Se o valor exceder o saldo, o sistema entra em cheque especial</li>
    <li>O usuário deve confirmar a operação</li>
    <li>O saldo pode ficar negativo</li>
    <li>Todas as operações são registradas no extrato</li>
</ul>

<h3>🚨 Cheque Especial</h3>

<h4>❓ O que é</h4>
<ul>
    <li>Permite sacar dinheiro mesmo sem saldo disponível</li>
    <li>O saldo negativo representa uma dívida com o banco</li>
</ul>

<h4>⚙️ Funcionamento</h4>
<ul>
    <li>Ativado automaticamente quando o saque excede o saldo</li>
    <li>O usuário deve confirmar a operação</li>
    <li>Após a confirmação, o saldo fica negativo</li>
</ul>

<h4>📊 Porcentagem de Juros</h4>
<ul>
    <li>Taxa fixa de <strong>1%</strong> sobre o valor da dívida</li>
    <li>A taxa não é cobrada no saque</li>
    <li>Ela é aplicada no momento do depósito</li>
</ul>

<h4>🧮 Cálculo da Taxa</h4>
<ul>
    <li>Taxa = valor absoluto do saldo negativo × 0.01</li>
</ul>

<h4>📘 Exemplo</h4>
<ul>
    <li>Saldo: -R$ 200,00</li>
    <li>Taxa (1%): R$ 2,00</li>
    <li>Depósito de R$ 100,00 resulta em R$ 98,00 líquido</li>
    <li>Novo saldo: -R$ 102,00</li>
</ul>

<h4>🧾 Registro no Extrato</h4>
<ul>
    <li>Saques no cheque especial são identificados</li>
    <li>Depósitos com taxa aparecem detalhados</li>
</ul>

<h3>📄 Extrato</h3>
<ul>
    <li>Exibe todas as movimentações realizadas</li>
    <li>Mostra depósitos, saques e cheque especial</li>
    <li>Exibe o saldo final da conta</li>
    <li>Informa quando não há movimentações</li>
</ul>

<h2>⚠️ Regras do Sistema</h2>
<ul>
    <li>Saldo inicial: R$ 0,00</li>
    <li>Limite de saque: R$ 500,00</li>
    <li>Máximo de 3 saques</li>
    <li>Taxa de 1% aplicada sobre saldo negativo</li>
</ul>

<h2>▶️ Como Executar</h2>
<ul>
    <li>Ter Python 3 instalado</li>
    <li>Salvar o arquivo como banco.py</li>
    <li>Executar: python banco.py</li>
</ul>

<h2>🎯 Objetivo Educacional</h2>
<ul>
    <li>Praticar lógica de programação</li>
    <li>Aplicar estruturas condicionais</li>
    <li>Utilizar laços de repetição</li>
    <li>Simular regras bancárias reais</li>
</ul>

<h2>👤 Autor</h2>
<ul>
    <li>Leandro Cruz</li>
</ul>
