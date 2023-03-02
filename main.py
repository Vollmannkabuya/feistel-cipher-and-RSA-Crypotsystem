from fonctionFeistelEtRSA import feistel_keygen, feistel_encrypt, feistel_decrypt, generate_keys, encrypt, decrypt

print("\n\n================================================================\n")
print("BIENVENU DANS NOTRE PROGRAMME\nTransmission des données et la sécurité informatique")
print("Laboratoire de la Cryptographie\n")
menu = int(input("entrez l'algorithme de chiffrement que vous souhaiter exécuter: \nPour Le chiffrement de Feistel tapez 1\nPour Le chiffrement RSA tapez 2 :  \n\n===>>"))

if menu == 1:
    K = input("Entrez la clé K de longueur 8 ex: 11001010\n")
    N1 = input("Entrez le bloc N de 8 bits ex: 00110011\n\n")
        
    # Convertir les entrées en listes
    K = [int(x) for x in K]
    N1 = [int(x) for x in N1]
    temp = input("\n\nVoulez-vous configurer l'algorithme? entrez: \noui pour configurer et \nnon pour utiliser des valeurs par defaut: \n\n===>>")
    k1,k2 = feistel_keygen([1,1,1,0,1,1,0,0],2,1)
    if temp == "oui":
        perm_h = input("\n\nEntrez la permutation H pour la generation de clé, ex= 65274130 :\n===>>")
        perm_pi = input("Entrez la permutation π pour le chiffrement et déchiffrement ex= 46027315:\n===>>")

        # Convertir les entrées en listes
        perm_h = [int(x) for x in perm_h]
        perm_pi = [int(x) for x in perm_pi]

        left_shift_order = int(input("Entrez l'ordre de décalage à gauche : "))
        right_shift_order = int(input("Entrez l'ordre de décalage à droite : "))

        #appel de trois fonction (algorithme de Feistel)  avec argument personalisé
        k1,k2 = feistel_keygen(K,left_shift_order,right_shift_order,perm_h)
        C = feistel_encrypt(N1,k1,k2,perm_pi)
        N2 = feistel_decrypt(C,k1,k2,perm_pi)
        print("\n\nLe bloc N de 8 bits",N1,"\nLe texte chiffré C de longueur 8. =",C,"\nLe texte clair N de longueur 8.",N2)
    
    elif temp == "non":
        #appel de trois fonction (algorithme de Feistel ) sans argument
        k1,k2 = feistel_keygen(K)
        C = feistel_encrypt(N1,k1,k2)
        N2 = feistel_decrypt(C,k1,k2)
        print("\n\nLe bloc N de 8 bits",N1,"\nLe texte chiffré C de longueur 8. =",C,"\nLe texte clair N de longueur 8.",N2)

    else:
        print("merci de bien répondre svp")

        
elif menu == 2:
    #Le chiffrement RSA
    p = int(input("entrez un nombre premier p ex= 59 61 67 71 73 79 83 89 97\n===>>"))
    q = int(input("entrez un nombre premier q différent de p\n===>>"))

    # Génération des clés
    public_key, private_key = generate_keys(p, q)

    # Chiffrement d'un message
    message = input("ecrivez le message à chiffrer:  \n===>>")
    cipher = encrypt(message, public_key)
    #block non pris en compte pour l'instant
    block = input("entrez le block de chiffrement que vous souhaitez (256, 512 ou 1024)\n===>>")
    # Déchiffrement du message chiffré
    decrypted_message = decrypt(cipher, private_key)

    print("Message original :", message)
    print("Message chiffré :", cipher)
    print("Message déchiffré :", decrypted_message)
    
else:
    print("veuillez choisir le bon numero")

    