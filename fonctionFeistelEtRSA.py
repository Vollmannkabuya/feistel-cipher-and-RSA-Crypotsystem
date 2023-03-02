
import random
import math

#Question 1 : Le chiffrement de Feisteil

#Algorithme pour la génération des clés
def feistel_keygen(key,left_shift=2, right_shift=1, perm_h = [6, 5, 2, 7, 4, 1, 3, 0]):
    # Application de la permutation H fixe
    h_key = [key[perm_h[i]] for i in range(8)]

    # Division de la clé en deux blocs de 4 bits
    k1_prime = h_key[:4]
    k2_prime = h_key[4:]

    # Calcul des sous-clés k1 et k2
    k1 = [k1_prime[i] ^ k2_prime[i] for i in range(4)]
    k2 = [k2_prime[i] & k1_prime[i] for i in range(4)]

    # Décalage des sous-clés
    k1_shifted = k1[left_shift:] + k1[:left_shift]
    k2_shifted = k2[-right_shift:] + k2[:-right_shift]

    return k1_shifted, k2_shifted



def inverse_permutation(perm):
        """
        Pour trouver l'inverse de la permutation, on doit créer une nouvelle permutation 
        qui inverse l'effet de la permutation d'origine. Pour ce faire, 
        on peut créer une nouvelle liste d'éléments où chaque élément représente 
        la position de l'élément correspondant dans la permutation d'origine.

        Pour illustrer cela, prenons l'exemple de l'élément à la position 0 dans la permutation d'origine. 
        Cet élément est 4. Dans la nouvelle permutation, la position de l'élément 4 doit être 0. 
        Ainsi, on place l'élément 0 à la position 4 dans la nouvelle permutation.
        """
        n = len(perm)
        inv = [0] * n

        for i in range(n):
            inv[perm[i]] = i

        return inv

#les fonction concernant le chiffrement RSA

#Algorithme de chiffrement
def feistel_encrypt(N,k1,k2,perm_pi=[4, 6, 0, 2, 7, 3, 1, 5]):
    # Application de la permutation π
    pi_N = [N[perm_pi[i]] for i in range(8)]

    # Division du bloc en deux parties
    G = pi_N[:4]
    D = pi_N[4:]

    # Premier round
    P = [2, 0, 1, 3] # permutation fixe

    GP = [G[P[i]] for i in range(4)] #permutation de G

    D1 = [GP[i] ^ k1[i] for i in range(4)]

    G1 = [D[i] ^ (G[i] | k1[i]) for i in range(4)]


    # Deuxième round
    G1P = [G1[P[i]] for i in range(4)] #permutation de G

    D2 = [G1P[i] ^ k2[i] for i in range(4)]

    G2 = [D1[i] ^ (G1[i] | k2[i]) for i in range(4)]
    # Concaténation des blocs G2 et D2
    C = G2 + D2
    # Application de l'inverse de la permutation π^-1
    perm_pi_inv = inverse_permutation(perm_pi)

    C = [C[perm_pi_inv[i]] for i in range(8)]

    return C


def feistel_decrypt(C,k1,k2,perm_pi = [4, 6, 0, 2, 7, 3, 1, 5]):
    

    # Application de la permutation π
    pi_C = [C[perm_pi[i]] for i in range(8)]

    # Division du bloc en deux  parties
    G2 = pi_C[:4]
    D2 = pi_C[4:]

    # Premier round

    P = [2, 0, 1, 3] # permutation fixe
    Pi = inverse_permutation(P)
    # P est maintenant une permutation inverse
    G1 = [D2[i] ^ k2[i] for i in range(4)]
    G1 = [G1[Pi[i]] for i in range(4)]
    D1 = [G2[i] ^ (G1[i] | k2[i]) for i in range(4)]

    # Deuxième round    
    G0 = [D1[i] ^ k1[i] for i in range(4)]
    G0 = [G0[Pi[i]] for i in range(4)]
    D0 = [G1[i] ^ (G0[i] | k1[i]) for i in range(4)]

    # Concaténation des blocs G0 et D0
    N = G0 + D0

    # Application de l'inverse de la permutation π^-1
    perm_pi_inv = inverse_permutation(perm_pi)
    N = [N[perm_pi_inv[i]] for i in range(8)]

    return N

def is_prime(n):
    """Vérifie si un nombre est premier."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True



def generate_keys(p, q):
    """Génère les clés RSA à partir de deux nombres premiers p et q."""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p et q doivent être des nombres premiers")
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Cherche un exposant de chiffrement e tel que 1 < e < phi_n et gcd(e, phi_n) = 1
    while True:
        e = random.randint(2, phi_n - 1)
        if math.gcd(e, phi_n) == 1:
            break

    # Calcul de l'inverse de e modulo phi_n
    d = pow(e, -1, phi_n)

    # Clé publique (e, n) et clé privée (d, n)
    return (e, n), (d, n)

def encrypt(message, public_key):
    """Chiffre un message en utilisant la clé publique."""
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    """Déchiffre un message en utilisant la clé privée."""
    d, n = private_key
    message = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(message)


