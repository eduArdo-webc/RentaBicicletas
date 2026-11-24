# Renta de bicicletas

Programa en Python que usa funciones para calcular el cobro de la renta de bicicletas en un parque.

| Tipo de bicicleta | Costo por hora |
|---|---|
| Estandar | $30 |
| Montana | $50 |
| Electrica | $80 |

Si la renta es de 4 horas o mas, se aplica un descuento del 15%.

Funciones:

1. `calcular_costo(precio, horas)` - regresa el costo de la renta.
2. `calcular_descuento(costo, horas)` - regresa el descuento (15% si son 4 horas o mas).
3. `calcular_total(costo, descuento)` - regresa el total a pagar.

## Como correrlo

```
python renta_bicicletas.py
```
