from conexao import connection
import csv

def extracao():
    conn = connection()
    cur = conn.cursor()

    query = """
    
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
    