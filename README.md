# 💳 Simulador Completo de Parcelamento com Streamlit

Este projeto é uma aplicação em Python usando Streamlit para simular cenários de vendas parceladas no cartão de crédito, considerando taxas da operadora e juros adicionais ao cliente.

---

## ✨ Funcionalidades

✅ **Venda Bruta (quanto recebo)**
- Você informa o valor bruto da venda.
- O sistema calcula:
  - Valor líquido que a loja recebe após taxas.
  - Valor da parcela do cliente.
  - Total pago pelo cliente.

✅ **Venda Líquida (quanto cobrar)**
- Você informa o valor líquido que deseja receber.
- O sistema calcula:
  - O valor bruto que deve ser cobrado.
  - Parcela e total pago pelo cliente.

✅ **Tabela Comparativa (cenários repassando e assumindo taxa)**
- Você informa o valor líquido desejado.
- O sistema gera uma tabela de 2x a 18x mostrando:
  - Cenário A: repassando a taxa ao cliente (você recebe o líquido integral).
  - Cenário B: assumindo a taxa (o cliente paga o valor base).
  - Parcelas, total pago e líquidos em cada cenário.
- Opção de incluir juros adicionais ao cliente.

---

## 🛠 Tecnologias Utilizadas

- Python 3.x
- Streamlit
- Pandas

---

## 🚀 Como executar

1. Instale as dependências (se ainda não tiver):
