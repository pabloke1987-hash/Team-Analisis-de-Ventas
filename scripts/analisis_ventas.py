import pandas as pd

df = pd.read_csv('datos/ventas.csv')

df['total'] = df['cantidad'] * df['precio']

ventas_totales = df['total'].sum()

producto_top = df.groupby('producto')['cantidad'].sum().idxmax()

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_top)

df.to_csv('resultados/salida.csv', index=False)
