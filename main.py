import pandas as pd
import numpy as np

# Criar um array numpy
data = np.array ([[1,2,3], [4,5,6], [7,8,9]])

# Criar um DataFrame a partir do array numpy
df = pd.DataFrame(data, columns=['Coluna1', 'Coluna2', 'Coluna3'])

# Exibir o DataFrame
print(df)
