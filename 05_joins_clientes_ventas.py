import pandas as pd


clientes = pd.DataFrame(
    {
        "id_cliente": [1, 2, 3],
        "nombre": ["Ana Pérez", "Luis Gómez", "Carla Díaz"],
        "ciudad": ["Quito", "Cuenca", "Guayaquil"],
    }
)

ventas = pd.DataFrame(
    {
        "id_venta": [101, 102, 103],
        "id_cliente": [1, 2, 3],
        "monto": [300, 450, 200],
    }
)

clientes_con_ventas = pd.merge(clientes, ventas, on="id_cliente", how="left")
ventas_con_clientes = pd.merge(clientes, ventas, on="id_cliente", how="right")

print("Clientes, incluso si no tienen ventas:")
print(clientes_con_ventas.to_string(index=False))
print("\nVentas, incluso si el cliente no existe:")
print(ventas_con_clientes.to_string(index=False))
