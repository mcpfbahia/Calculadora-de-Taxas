import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simulador Parcelamento Completo", layout="wide")
st.title("💳 Simulador Completo de Venda Parcelada")

st.write("""
✅ Venda Bruta ➜ calcula quanto recebe líquido  
✅ Venda Líquida ➜ calcula quanto cobrar para receber o valor desejado  
✅ Tabela Comparativa ➜ mostra todos os cenários (repassando ou assumindo taxa)
""")

# Tabela de taxas (%)
taxas = {
    2: 5.11,
    3: 5.74,
    4: 6.39,
    5: 7.12,
    6: 7.81,
    7: 8.74,
    8: 9.59,
    9: 10.53,
    10: 11.19,
    11: 12.14,
    12: 13.11,
    13: 14.47,
    14: 15.33,
    15: 16.19,
    16: 17.05,
    17: 17.91,
    18: 18.77
}

# Modo de simulação
modo = st.radio(
    "Selecione o tipo de simulação:",
    [
        "Venda Bruta (quanto recebo)",
        "Venda Líquida (quanto cobrar)",
        "Tabela Comparativa (cenários repassando e assumindo taxa)"
    ]
)

# Entrada de juros adicionais
juros_cliente = st.number_input(
    "📈 Juros adicionais ao cliente (% ao mês):",
    min_value=0.0,
    format="%.2f"
)

if modo == "Venda Bruta (quanto recebo)":
    st.subheader("💰 Simulação a partir do valor bruto da venda")

    valor_venda = st.number_input(
        "💰 Valor bruto da venda (R$):",
        min_value=0.0,
        format="%.2f"
    )
    parcelas = st.slider(
        "Parcelas:",
        min_value=2,
        max_value=18,
        value=6
    )

    if valor_venda > 0:
        taxa = taxas[parcelas] / 100
        liquido = valor_venda * (1 - taxa)
        parcela_base = valor_venda / parcelas

        if juros_cliente > 0:
            i = juros_cliente / 100
            parcela_cliente = (
                (valor_venda * i * (1 + i) ** parcelas)
                / ((1 + i) ** parcelas - 1)
            )
            total_pago = parcela_cliente * parcelas
        else:
            parcela_cliente = parcela_base
            total_pago = valor_venda

        st.success(f"✅ Taxa total: {taxas[parcelas]:.2f}%")
        st.info(f"💸 Valor líquido que você recebe: R$ {liquido:,.2f}")
        st.warning(
            f"💵 Cliente pagará {parcelas}x de R$ {parcela_cliente:,.2f} "
            f"(total R$ {total_pago:,.2f})"
        )

elif modo == "Venda Líquida (quanto cobrar)":
    st.subheader("💰 Simulação a partir do valor líquido desejado")

    valor_liquido = st.number_input(
        "💸 Valor líquido desejado (R$):",
        min_value=0.0,
        format="%.2f"
    )
    parcelas = st.slider(
        "Parcelas:",
        min_value=2,
        max_value=18,
        value=6,
        key="parcelas_liquido"
    )

    if valor_liquido > 0:
        taxa = taxas[parcelas] / 100
        bruto_necessario = valor_liquido / (1 - taxa)

        if juros_cliente > 0:
            i = juros_cliente / 100
            parcela_cliente = (
                (bruto_necessario * i * (1 + i) ** parcelas)
                / ((1 + i) ** parcelas - 1)
            )
            total_pago = parcela_cliente * parcelas
        else:
            parcela_cliente = bruto_necessario / parcelas
            total_pago = bruto_necessario

        st.success(f"✅ Taxa total: {taxas[parcelas]:.2f}%")
        st.info(f"💰 Valor bruto que deve ser cobrado: R$ {bruto_necessario:,.2f}")
        st.warning(
            f"💵 Cliente pagará {parcelas}x de R$ {parcela_cliente:,.2f} "
            f"(total R$ {total_pago:,.2f})"
        )

elif modo == "Tabela Comparativa (cenários repassando e assumindo taxa)":
    st.subheader("📊 Tabela comparativa: repassando e assumindo taxa")

    valor_liquido = st.number_input(
        "💸 Valor líquido desejado (R$):",
        min_value=0.0,
        format="%.2f",
        key="valor_tabela_liquido"
    )

    if valor_liquido > 0:
        dados = []
        for n_parc in range(2, 19):
            taxa = taxas[n_parc] / 100

            # Cenário A - Repassando taxa ao cliente
            bruto_repassando = valor_liquido / (1 - taxa)
            liquido_repassando = bruto_repassando * (1 - taxa)

            if juros_cliente > 0:
                i = juros_cliente / 100
                parcela_com_juros_repassando = (
                    (bruto_repassando * i * (1 + i) ** n_parc)
                    / ((1 + i) ** n_parc - 1)
                )
                total_com_juros_repassando = parcela_com_juros_repassando * n_parc
            else:
                parcela_com_juros_repassando = bruto_repassando / n_parc
                total_com_juros_repassando = bruto_repassando

            # Cenário B - Loja assume taxa
            bruto_assumindo = valor_liquido
            liquido_assumindo = bruto_assumindo * (1 - taxa)

            if juros_cliente > 0:
                i = juros_cliente / 100
                parcela_com_juros_assumindo = (
                    (bruto_assumindo * i * (1 + i) ** n_parc)
                    / ((1 + i) ** n_parc - 1)
                )
                total_com_juros_assumindo = parcela_com_juros_assumindo * n_parc
            else:
                parcela_com_juros_assumindo = bruto_assumindo / n_parc
                total_com_juros_assumindo = bruto_assumindo

            dados.append({
                "Parcelas": f"{n_parc}x",
                "Taxa (%)": f"{taxas[n_parc]:.2f}",
                "Bruto p/ Receber Líquido": f"{bruto_repassando:,.2f}",
                "Parcela Cliente (Repassando)": f"{parcela_com_juros_repassando:,.2f}",
                "Total Cliente (Repassando)": f"{total_com_juros_repassando:,.2f}",
                "Bruto (Assumindo)": f"{bruto_assumindo:,.2f}",
                "Parcela Cliente (Assumindo)": f"{parcela_com_juros_assumindo:,.2f}",
                "Total Cliente (Assumindo)": f"{total_com_juros_assumindo:,.2f}",
                "Líquido (Assumindo)": f"{liquido_assumindo:,.2f}",
            })

        df = pd.DataFrame(dados)
        st.dataframe(df, use_container_width=True)
