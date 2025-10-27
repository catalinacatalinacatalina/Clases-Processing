# 📝 Cheatsheet de Listas
## 1️⃣ Crear listas
- listas vacías
    ```python
    lista_vacia = []
    otra_lista = list()
    ```
- listas con elementos que ya tenemos
    ```
    numeros = [1, 2, 3, 4]
    frutas = ["manzana", "banana", "cereza"]
    ```


## 2️⃣ Acceso a elementos

```python
frutas[0]   # primer elemento → "manzana"
frutas[-1]  # último elemento → "cereza"
```
A tener en cuenta:

- Los índices empiezan en 0.
- El índice `-1` accede al último elemento.

---

## 3️⃣ Modificar, añadir y eliminar

```python
frutas[1] = "kiwi"        # reemplaza "banana" por "kiwi"
frutas.append("naranja")  # añade al final
frutas.insert(1, "pera")  # añade en posición 1
frutas.pop()               # elimina el último elemento
frutas.pop(2)              # elimina el elemento en posición 2
```

- `insert(pos, valor)` añade en una posición concreta
-  `pop()` elimina y devuelve un elemento


## 4️⃣ Operaciones comunes

```python
len(frutas)            # longitud de la lista
sum([1,2,3])           # suma de los elementos (solo números)
max([1,5,2])            # máximo
min([1,5,2])            # mínimo
sorted([3,1,2])         # devuelve una lista ordenada (no modifica original)
frutas.reverse()        # invierte la lista en sitio
```

---

## 5️⃣ Recorrer listas

```python
# Recorrer por elementos
for fruta in frutas:
    print(fruta)

# Recorrer por índices
for i in range(len(frutas)):
    print(i, frutas[i])
```

- `for elemento in lista:` recorre cada elemento directamente
- `for i in range(len(lista)):` recorre usando índices (útil para modificar elementos)



## 6️⃣ Listas y funciones
- también le podemos pasar una lista a una funcion para que opere con ella.
    ```python
    def duplicar(lista):
        resultado = []
        for n in lista:
            resultado.append(n * 2)  # multiplica cada elemento por 2
        return resultado

    numeros = [1, 2, 3]
    print(duplicar(numeros))  # [2, 4, 6]
    ```

- Las listas se pueden pasar como argumento a funciones
- Se puede devolver una **lista nueva** sin modificar la original
