import matplotlib.pyplot as plt
import json

FILENAME = './results/test.json'

def plot(data):
    test_cases = data['test_cases']
    sizes = [d['SIZE'] for d in test_cases]
    slice_mean_times = [d['SLICE_MEAN_TIME'] for d in test_cases]
    index_mean_times = [d['INDEX_MEAN_TIME'] for d in test_cases]
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, slice_mean_times, marker='o', label="Slice (médio)")
    plt.plot(sizes, index_mean_times, marker='s', label="Indexado (médio)")
    plt.xlabel("Quantidade de elementos no array (N)")
    plt.ylabel("Tempo de execução (ms)")
    plt.title("Comparação Mergesort indexado e Mergesort com slice")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("./graphs/comparacao-mergesort.png", dpi=300)
    plt.show()

def get_data():
    data = None
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
        return data
    except:
        print(f"Não foi possível ler o arquivo {FILENAME}, verifique se ele existe")
        exit(1)

data = get_data()
plot(data)
