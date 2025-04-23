from conexao import connection
import csv

def extracao():
    conn = connection()
    cur = conn.cursor()

    query = """
    select
        se.cod_produto,
        p.nm_produto,
        e.descr_estoque,
        cc.descr_cc,
        se.data_saida,
        se.custo_unitario,
        se.qtd
    from sigh.saidas_estoques se 
    inner join sigh.produtos p 
        on p.id_produto = se.cod_produto
    inner join sigh.estoques e 
        on e.id_estoque = se.cod_estoque
    inner join sigh.centros_custos cc 
        on cc.id_centro_custo = se.cod_centro_custo
    where data_saida between '2023-01-01' and '2023-12-31'
    order by data_saida asc;
    """
    
    cur.execute(query)

    rows = cur.fetchall()

    csv_file = "C:/Users/Administrador/Desktop/projetos/dashboard_estoque_hsp/dados/dados.csv"

    with open(csv_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['cod_produto','nome_produto','estoque','centro_custo','data_saida','custo_unitario','quantidade'])
        writer.writerows(rows)

    cur.close()
    conn.close()


extracao()
    