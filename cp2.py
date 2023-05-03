# estoque inicial da vinheria
estoque = ["Vinho1", "vinho2"]

# pedidos iniciais da vinheria
pedidos = []
lista_de_compras = []

# MENU

inicio = True
while inicio:
    
    menu = input("[ESTOQUE]\n[PEDIDOS]\n[LISTA DE COMPRAS cod(LC)]\n")
    
    print("\n")
    print("\n")
    
    if menu == "ESTOQUE": # funcionalidades do estoque
        
        print(estoque) # exibe o estoque
        
        print("\n")
        print("\n")
        
        op2 = input("[MENU]\n[ADICIONAR]\n")
        
        if op2 == "MENU": # retorna ao menu principal
            inicio = True
            print("\n")
            print("\n")
            
            
        if op2 =="ADICIONAR": # adiciona um produto ao estoque
            adicionar = input("NOME DO PRODUTO: \n")
            estoque.append(adicionar)
            inicio = True
            print("\n")
            print("\n")
            
            
            
    if menu == "PEDIDOS": # funcionalidades dos pedidos
        op3 = input("[EXISTENTE]\n[NOVO]\n")
        print("\n")
        print("\n")
        
        if op3 == "EXISTENTE": # exibe os pedidos existentes
            
            if pedidos == []:
                print("[#NENHUM PEDIDO ENCONTRADO]")
                inicio = True
                print("\n")
                print("\n")
                
            else:
                print(pedidos)
                inicio = True
                print("\n")
                print("\n")
                
        elif op3 == "NOVO": # adiciona um novo pedido
            pedido = input("PEDIDO:\n ")
            pedidos.append(pedido)
            print("\n")
            print("\n")
            
            if pedido in estoque: # verifica se o produto está no estoque
                print("[#PRODUTO DESEJADO EM ESTOQUE] ")
                print("\n")
                print("\n")
                
            elif pedido not in estoque: # se o produto não estiver no estoque
                
                op4 = input("[#PRODUTO NAO ENCONTRADO NO ESTOQUE]\n[MENU]        [ADICIONAR PRODUTO A LISTA DE COMPRAS (cod: AD)]\n")
                
                
                if op4 == "MENU": # retorna ao menu principal
                    inicio = True
                    print("\n")
                    print("\n")
                    
                elif op4 == "AD": # adiciona o produto à lista de compras
                    lista_de_compras.append(pedido)
                    inicio = True
                    print("\n")
                    print("\n")
                
                else: # operação inválida
                    print("[#OPERAÇAO INVALIDA]")
                    
        else: # operação inválida
            print("[#OPERAÇAO INVALIDA]")
            inicio = True
            print("\n")
            print("\n")
            
            
    elif menu == "LC": # funcionalidades da lista de compras
         
         print(lista_de_compras) # exibe a lista de compras
         print("\n")
         print("\n")
          
         op5 = input("[ADICIONAR PRODUTO A LISTA DE COMPRAS cod(AD LC)]\n[MENU]\n")
         
         if op5 =="AD LC": # adiciona um produto à lista de compras
            op6 = input("PRODUTO A SER ADICIONADO: \n")
            lista_de_compras.append(op6)
            print("\n")
            print("\n")
            inicio = True
                 
         elif op5 == "MENU":
            inicio = True
            print("\n")
            print("\n")
                
         else:
            print("[#OPERAÇAO INVALIDA]")
            inicio = True