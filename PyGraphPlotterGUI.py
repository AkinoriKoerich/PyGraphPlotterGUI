import matplotlib.pyplot as plt
import tkinter as tk

def graph_line():
    def tracar_grafico():
        valor_x = entrada_x.get()
        valor_y = entrada_y.get()

        # Transforma os valores inseridos em uma lista de inteiros
        valores_x = [float(x.strip()) for x in valor_x.split(",")]
        valores_y = [float(y.strip()) for y in valor_y.split(",")]

        # Cria o gráfico de linha
        plt.plot(valores_x, valores_y)
        plt.show()

    janela = tk.Tk()
    janela.geometry("300x150")

    entrada_linha = tk.Label(janela, text='Digite apenas valores com virgula. Exemplo: "5,5" ')
    entrada_linha.pack()

    entrada_linha_x = tk.Label(janela, text="Eixo X")
    entrada_linha_x.pack()

    entrada_x = tk.Entry(janela)
    entrada_x.pack()

    entrada_linha_y = tk.Label(janela, text="Eixo Y")
    entrada_linha_y.pack()

    entrada_y = tk.Entry(janela)
    entrada_y.pack()

    botao_confirmar = tk.Button(janela, text="Confirmar", command=tracar_grafico)
    botao_confirmar.pack()

    # Iniciar a janela principal
    janela.mainloop()

def graph_bar():
    def tracar_grafico():
        num_barras = int(entrada_barras.get())
        valores_por_barra = [int(valor) for valor in entrada_valores.get().split(",")]
        plt.bar(range(num_barras), valores_por_barra)
        plt.show()
    janela = tk.Tk()
    janela.geometry("300x150")

    entrada_barras_label = tk.Label(janela, text="Número de barras")
    entrada_barras_label.pack()
    entrada_barras = tk.Entry(janela)
    entrada_barras.pack()

    entrada_valores_label = tk.Label(janela, text="Valores por barra (separados por vírgula)")
    entrada_valores_label.pack()
    entrada_valores = tk.Entry(janela)
    entrada_valores.pack()

    botao_confirmar = tk.Button(janela, text="Confirmar", command=tracar_grafico)
    botao_confirmar.pack()

    # Iniciar a janela principal
    janela.mainloop()

def graph_dispersion():
    def plot_points():
        x_vals = [float(x) for x in x_entry.get().split()]
        y_vals = [float(y) for y in y_entry.get().split()]
        plt.scatter(x_vals, y_vals)
        plt.show()
    root = tk.Tk()

    x_label = tk.Label(root, text="Valores X:")
    x_label.pack()
    x_entry = tk.Entry(root)
    x_entry.pack()

    y_label = tk.Label(root, text="Valores Y:")
    y_label.pack()
    y_entry = tk.Entry(root)
    y_entry.pack()

    plot_button = tk.Button(root, text="Plot", command=plot_points)
    plot_button.pack()

    root.mainloop()

def graph_area():
    # Cria uma janela
    janela = tk.Tk()
    janela.geometry("300x150")

    # Cria as entradas de valores para x e y
    entrada_x = tk.Entry(janela)
    entrada_x.pack()
    entrada_y = tk.Entry(janela)
    entrada_y.pack()

    # Função que é chamada quando o botão "Confirmar" é clicado
    def tracar_grafico():
        valores_x = [int(x.strip()) for x in entrada_x.get().split(",")]
        valores_y = [int(y.strip()) for y in entrada_y.get().split(",")]
        
        # Traça o gráfico de área com os valores fornecidos pelo usuário
        plt.stackplot(valores_x, valores_y, labels=['Área 1', 'Área 2'])
        plt.legend(loc='upper left')
        plt.show()

    # Cria o botão "Confirmar"
    botao_confirmar = tk.Button(janela, text="Confirmar", command=tracar_grafico)
    botao_confirmar.pack()

    # Iniciar a janela principal
    janela.mainloop()

def graph_histogram():
    def plot_histogram():
        # obter valores inseridos pelo usuário
        values_str = entrada_valores.get()
        # converter string de valores em uma lista de floats
        values = [float(x.strip()) for x in values_str.split(",")]

        # plotar o histograma
        plt.hist(values, bins=10)
        plt.xlabel('Valores')
        plt.ylabel('Frequência')
        plt.title('Histograma')
        plt.show()

    janela = tk.Tk()
    janela.geometry("300x150")

    entrada_valores = tk.Entry(janela)
    entrada_valores.pack()

    botao_confirmar = tk.Button(janela, text="Plotar", command=plot_histogram)
    botao_confirmar.pack()

    # Iniciar a janela principal
    janela.mainloop()

def graph_pie():
    def tracar_grafico():
        # Obter os valores digitados pelo usuário nas entradas de dados
        valores = []
        for entrada in entradas:
            valores.append(float(entrada.get()))

        # Traçar o gráfico de pizza
        fig1, ax1 = plt.subplots()
        ax1.pie(valores, labels=range(1, len(valores)+1), autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        plt.show()

    janela = tk.Tk()
    janela.geometry("300x150")

    # Entradas de dados para valores do gráfico
    entrada_quantidade = tk.Entry(janela)
    entrada_quantidade.pack()
    entradas = []
    botao_entradas = tk.Button(janela, text="Confirmar quantidade", command=lambda: adicionar_entradas(int(entrada_quantidade.get())))
    botao_entradas.pack()

    def adicionar_entradas(quantidade):
        for i in range(quantidade):
            entrada = tk.Entry(janela)
            entrada.pack()
            entradas.append(entrada)

        botao_confirmar = tk.Button(janela, text="Confirmar", command=tracar_grafico)
        botao_confirmar.pack()

    # Iniciar a janela principal
    janela.mainloop()



plt.style.use('ggplot')
root = tk.Tk()
root.title("Criador de Gráficos")
root.geometry("600x400")


# criar seção para seleção do tipo de gráfico
grafico_frame = tk.LabelFrame(root, text="Tipo de Gráfico")
grafico_frame.pack(padx=10, pady=10)

grafico_var = tk.StringVar()
grafico_var.set("Linha")

tk.Radiobutton(grafico_frame, text="Linha", variable=grafico_var, value="Linha", command=graph_line).pack(anchor="w")
tk.Radiobutton(grafico_frame, text="Barras", variable=grafico_var, value="Barras", command=graph_bar).pack(anchor="w")
tk.Radiobutton(grafico_frame, text="Dispersão", variable=grafico_var, value="Dispersão", command=graph_dispersion).pack(anchor="w")
tk.Radiobutton(grafico_frame, text="Área", variable=grafico_var, value="Área", command=graph_area).pack(anchor="w")
tk.Radiobutton(grafico_frame, text="Histograma", variable=grafico_var, value="Histograma", command=graph_histogram).pack(anchor="w")
tk.Radiobutton(grafico_frame, text="Pizza", variable=grafico_var, value="Pizza", command=graph_pie).pack(anchor="w")

# criar seção para inserção de dados
dados_var = tk.BooleanVar()
dados_var.set(False)

def toggle_dados():
    if dados_var.get():
        dados_frame.pack()
    else:
        dados_frame.pack_forget()

dados_checkbox = tk.Checkbutton(root, text="Inserir Dados", variable=dados_var, command=toggle_dados)
dados_checkbox.pack()

dados_frame = tk.LabelFrame(root, text="Inserção de Dados")

dados_label = tk.Label(dados_frame, text="Insira os dados do eixo x separados por vírgula:")
dados_label.grid(row=0, column=0)

dados_entry = tk.Entry(dados_frame)
dados_entry.grid(row=0, column=1)

dados_label = tk.Label(dados_frame, text="Insira os dados do eixo y separados por vírgula:")
dados_label.grid(row=1, column=0)

dados_entry = tk.Entry(dados_frame)
dados_entry.grid(row=1, column=1)

root.mainloop()
