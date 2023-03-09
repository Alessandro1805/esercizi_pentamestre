import random
class Node():
    def __init__(self,key):
        self.key=key
        self.left=None;
        self.right=None;
    def insert(self,key):
        pass
    def insertnode(self,key):
        if self.key:
            if key > self.key:
                if self.right is None:
                    self.right=Node(key)
                else:
                    self.right.insertnode(key)
            elif key< self.key:
                if self.left is None:
                    self.left=Node(key)
                else:
                    self.left.insertnode(key)
    def printree(self,level=0):
        if self.left is not None:
            self.left.printree (level+1)
        print(f"level{level} ->{self.key}")
        if self.right is not None:
            self.right.printree(level+1)
    def findnode(self, key):
        if key>self.key:
            if self.right==None:
                return f"Nodo {key} non trovato"
            return self.right.ricercaDicotomica(key)
        elif key<self.key:
            if self.left is None:
                return f"Nodo {key} non trovato"
            return self.left.ricercaDicotomica(key)
        else:
            return f"nodo {key} trovato"                 
    def implementa_albero_bilanciato():
        pass
    def contaltezza(self,livellod,livellos):
        if self.right!=None:
            return self.right.contaltezza(livellod+1,livellos)
        elif self.left!=None:
            return self.left.contaltezza(livellod,livellos+1)
        else:
            if livellos>livellod:
                return livellos+1
            else:
                return livellod+1
                
def build_tree(nodes):
    l=len(nodes)##i valori di nodes devono essere ordinati crescenti
    if l==0:
        return None
    nodes.sort()##complessità di tempo o di n alla seconda porta via tempo
    medium_point=l//2
    root=Node(nodes[medium_point])
    root.left=build_tree(nodes[0:medium_point])
    root.right=build_tree(nodes[medium_point+1:])
    return root
def main():
    lista_key=list(range(0,40,5))
    random.shuffle(lista_key)
    albero=build_tree(lista_key)
    albero.printree()
    print(albero.contaltezza(0,0))
if __name__=="__main__":
    main()