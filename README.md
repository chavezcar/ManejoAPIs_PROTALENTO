# Consumo de de APIs - Ejercicio Práctico PROTALENTO.

> ### Construcción de la solución para el laboratorio propuesto.

>  *Laboratorio APIs*: Se debe crear código en **Python** con las siguientes indicaciones:>
> - Cargar el data frame **currency_codes.csv** y retornar los ISO codes (usando la columna AlphabeticCode) como una lista. Referencia sobre ISO codes: <https://en.wikipedia.org/wiki/List_of_circulating_currencies> a una lista de Python.
> - Realizar múltiples consultas para obtener los tipos de cambio **USD_(ISO_CODE)** <https://api-ninjas.com/api/exchangerate> para luego guardarlos en un dataframe con las columnas **(iso_code, tipo_de_cambio)**, exporta el resultado como un **monedas.csv**.
> - Carga el csv en la función correspondiente. Recibirás como argumento dos monedas en formato **ISO** y el monto a convertir, debes retornar el nuevo monto convertido. Recuerda que tienes el tipo de cambio de las monedas de USD a cualquiera, así que primero debes convertir la moneda de origen a USD y luego de USD a la moneda de destino.
