# Capítulo 0 - Contextualização Problema de Identificação de Sistema Dinâmico

## 1. Sistema Dinâmico

Em geral, tem-se y=h(x), sem ter uma dependência direta do vetor de entrada/controlo u_c

$$
\dot{x} = f(x, u_c, \lambda) + \epsilon
$$
$$
y = h(x) + \eta
$$

f e h são funções determinísticas, $\eta$ e $\epsilon$ são vetores aleatórios.

## 2. Problemática da Identificação de Sistemas Dinâmicos

Tendo medições y(t_0), y(t_1), ..., y(t_n) nos instantes t_0, t_1, ..., t_n, o problema de identificação consiste em estimar/"encontrar" os valores dos elementos (i.e. de cada elemento) do vetor de parâmetros $\lambda$.

De facto, o objetivo final é caracterizar o sistema pelo conhecimento de valores do vetor $\lambda$ em cada instante.

## 3. Identificabilidade

### (Capacidade de identificar um sistema)

- Será que podemos identificar qualquer sistema dinâmico em qualquer contexto?
-- Resposta rápida: **Nem sempre**

#### Em que medida é que se pode garantir a identificabilidade do sistema?

- É possível identificar o sistema se e só se o seu modelo (no espaço de estado) for observável. (VER APONTAMENTOS DVS)

$$
\dot{x} = f(x, u, \lambda)
$$
$$
\dot{\lambda} = 0
$$
$$
y = h(x)
$$

(Não consideramos as incertezas)

Este modelo é observável se e só se se pode determinar/estimar os valores dos vetores x e $\lambda$ com base das medições do vetor y ao longo do tempo.

**De concreto**, no domínio aeroespacial, recorre-se ao seguinte caso em que se garante a possibilidade de identificar o sistema:
$h(x) = x$

Implica que $y = x + \eta$

## 4. Contexto de Dinâmica de Voo

### Identificação de Modelo de Dinâmica de Voo

Considerando  padrão do modelo da Dinâmica do Voo, temos

$\dot{x} = A(\lambda)x + B(\lambda)u_c + \epsilon$

$y = x + \eta$

$A(\lambda)$ e $B(\lambda)$ são matrizes cujos elementos dependem do vetor de parâmetros $\lambda$: vetor composto pelas derivadas de estabilidade e de controlo. 

# Capítulo 1 - Probabilidades e Estatística
