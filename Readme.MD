# Descenso de gradiente con varios mínimos locales

Pequeño experimento en Python para ver cómo el **descenso de gradiente** puede acabar en mínimos distintos según el punto de partida y el *learning rate*.

## La función

```
f(x)  = x⁴ − 4x² + x
f'(x) = 4x³ − 8x + 1
```

Tiene dos mínimos locales:

| Punto | x aproximada | f(x) aproximada |
|---|---|---|
| Mínimo global | −1,47 | −5,45 |
| Mínimo local | 1,35 | −2,62 |

## Cómo funciona

El algoritmo parte de un punto `x` y lo va actualizando en dirección contraria a la pendiente:

```
x = x − learning_rate · f'(x)
```

El script ejecuta el descenso desde varios puntos iniciales (`-2.5`, `0` y `2.5`), con `learning_rate = 0.1` y 10 iteraciones, y dibuja la función con:

- 🟢 el **mínimo global** encontrado (el de menor `f(x)`)
- 🔴 los **mínimos locales** (puntos finales que no coinciden con el global)

## Cómo ejecutarlo

```bash
pip install numpy matplotlib
python descenso_gradiente.py
```

## Resultados

| Punto inicial | Punto final | f(x) |
|---|---|---|
| −2,5 | 1,35 | −2,62 (mínimo local) |
| 0 | −1,45 | −5,44 (≈ mínimo global) |
| 2,5 | −1,48 | −5,44 (≈ mínimo global) |

## Conclusiones

- El **punto de partida** decide a qué mínimo llegas: el descenso de gradiente no garantiza encontrar el mínimo global.
- El **learning rate** importa mucho. Con `0.1`, partiendo de −2,5 (pendiente muy fuerte) el primer paso salta al otro lado de la colina y acaba en el mínimo local, al revés de lo que cabría esperar. Con `0.01` y más iteraciones, ese mismo punto llega al mínimo global.
- Comparar los mínimos hay que hacerlo por el valor de la función (`f(x)`), no por la posición `x`.
- Con pocas iteraciones el algoritmo puede no haber convergido del todo (por eso el punto final desde 0 es −1,45 y no −1,47).

## Ideas para ampliarlo

- Probar distintos valores de `learning_rate` y número de iteraciones.
- Dibujar la trayectoria completa de cada descenso sobre la curva.
- Añadir *momentum* y ver si consigue superar la colina.
- Pasar a dos variables y visualizar la superficie en 3D.