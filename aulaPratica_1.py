import math
import numpy as np

def media(lista):
    return sum(lista) / len(lista)

def variancia(lista):
    m = media(lista)
    return sum((x - m) ** 2 for x in lista) / (len(lista) - 1)

def desvio_padrao(lista):
    return math.sqrt(variancia(lista))

# Dados das variáveis de voo

u = [32.15, 33.1, 34.05, 36.18, 38.85, 39.14,
        40.72, 42.83, 44.55, 45.91, 44.87, 44.02,
        43.65, 42.96, 42.05, 41.2]

w = [0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0, 0, 0, 0,
        -0.05, -0.1, -0.15, -0.05, 0]

q = [0.05, 0.03, 0.03, 0.02, 0.02, 0.01, 0.01, 0.00, 0.00,
        0.00, 0.00, -0.06, -0.13, -0.19, -0.06, 0.00]

theta = [0.35, 0.36, 0.36, 0.36, 0.36, 0.37, 0.37, 0.37,
            0.37, 0.37, 0.37, 0.37, 0.36, 0.35, 0.33, 0.32]

### EXERCICIO 1

media_u = media(u)
variancia_u = variancia(u)
desvio_u = desvio_padrao(u)

media_w = media(w)
variancia_w = variancia(w)
desvio_w = desvio_padrao(w)

media_q = media(q)
variancia_q = variancia(q)
desvio_q = desvio_padrao(q)

media_theta = media(theta)
variancia_theta = variancia(theta)
desvio_theta = desvio_padrao(theta)

print(f"u: média={media_u:.4f}, variância={variancia_u:.4f}, desvio padrão={desvio_u:.4f}")
print(f"w: média={media_w:.4f}, variância={variancia_w:.4f}, desvio padrão={desvio_w:.4f}")
print(f"q: média={media_q:.4f}, variância={variancia_q:.4f}, desvio padrão={desvio_q:.4f}")
print(f"theta: média={media_theta:.4f}, variância={variancia_theta:.4f}, desvio padrão={desvio_theta:.4f}")

### EXERCICIO 2
cov_uw = np.cov(u, w)

print(f"Covariância entre u e w:\n{cov_uw}")

### EXERCICIO 3

x = np.array([u, w, q, theta])
cov_x = np.cov(x)
print("Matriz de covariância do vetor x= (u w q theta)T:")
print(cov_x)