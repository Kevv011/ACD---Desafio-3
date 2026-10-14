import pandas as pd


data = {
    "id_venta": [1, 2, 3, 4],
    "fecha_venta": ["2024-01-10", "2024-01-10", "2024-01-11", "2024-01-11"],
    "id_cliente": [100, 101, 100, 102],
    "producto": ["Teclado", "Mouse", "Monitor", "Teclado"],
    "cantidad": [2, 1, 1, 3],
    "precio_unitario": [15, 10, 120, 15],
}

ventas = pd.DataFrame(data)
ventas["total_venta"] = ventas["cantidad"] * ventas["precio_unitario"]
total_por_producto = (
    ventas.groupby("producto", as_index=False)["total_venta"]
    .sum()
    .sort_values("total_venta", ascending=False)
)

print(total_por_producto.to_string(index=False))
