import os

class Node:
    def __init__(self, afm=None,product=None,total=None):
        self.afm = afm
        self.product = product
        self.total = total
        self.left = None
        self.right = None        
# A utility function to insert a new node with the given key
def insert(root,node): 
    if root is None: 
        root = first(node) 
    else:
        if root.afm == node.afm:
            notfound=True

            for i in range(len(node.product)):
                for j in range(len(root.product)):
                    if node.product[i]==root.product[j]:
                        root.total[j]+=node.total[i]
                        root.total[j]=round(root.total[j],2)
                        notfound=False
                if notfound:
                    root.product.append(node.product[i])
                    root.total.append(node.total[i])
        elif root.afm < node.afm: 
            if root.right is None: 
                root.right = first(node)
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = first(node) 
            else: 
                insert(root.left, node)

def first (node1):
        #print(node1.afm,node1.product,node1.total)
        newName=[0]
        newSum=[0]
        flag2=False
        for i in range(len(node1.product)):
            sum=node1.total[i]
            for k in range(i):
                #print(node1.product[i],node1.product[k])
                if node1.product[i]==node1.product[k]:
                    flag2=True
            if not flag2:
                for j in range(i+1,len(node1.product)):
                    #print(j)
                    if node1.product[i]==node1.product[j]:
                        sum=sum+node1.total[j]
                                                
                newName.append(node1.product[i])
                newSum.append(sum)
                
            flag2=False
        help=(Node(node1.afm,newName[1:len(newName)],newSum[1:len(newSum)]))
        #print(help.afm,help.product,help.total)
        return help
# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.afm) 
        print(root.product) 
        print(root.total)
        inorder(root.right)
# A utility function to do inorder tree traversal 
def inordersearch(root,product): 
    if root: 
        inordersearch(root.left,product) 
        for i in range(len(root.product)):
            if root.product[i]==product:
                print(root.afm,root.total[i])
        inordersearch(root.right,product)
# A utility function to search a given key in BST 
def search(root,key): 
      
    # Base Cases: root is null or key is present at root 
    if root is None or root.afm == key: 
        return root 
  
    # Key is greater than root's key 
    if root.afm < key: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key) 

def checkafm(cdeka):

    line=" ".join(cdeka.split())
    #print(line)
    if len(line)==15:
        afm=line[5:15]
        if afm.isdigit():
          return afm      
    return 0

def cproion(proion):
    line=" ".join(proion.split())
    count=0
    while (line[count]) != (":") :
        count+=1
    proionta=line[count+2:len(line)]
    inf=line[0:count]
    info=[0,0,0,0]
    info[0]=inf
    info[0]=info[0].upper()
    array=proionta.split()
    info[1]=int(array[0])
    info[2]=float(array[1])
    info[3]=float(array[2])
    apotelesma=round(float(info[1] * info[2]),2)
    if (apotelesma == info[3]):
        return info
    return 0


flagAr=True
while True:

    try:
        choice= int(input("Give your preference: \n1: read new input file\n2: print statistics for a specific product\n3: print statistics for a specific AFM\n4: exit the program:\t"))
    except :
        continue

    flag=False
    
    if choice==1 :
        filename=input("Enter the file name:\t")
        filename=filename + ".txt"
        try:
            file = open(filename,encoding='utf-8')
            #print (file.read())
        except IOError:
            print ('\ndoes not exist!!\n')
            continue
        line=5
        line = (file.readline())
       #line = (file.readline())
        #print(line)
        cnt = 1
        valeproion=0
        flag=True
        flag2=False
        counterpaules=0
        ekxor=0
        while line:
            if line[0:6] == "------" :
                counterpaules+=1
                line = file.readline()
                afm=checkafm(line)
                if afm:
                    line = file.readline()
                    sunolo=0
                    counter=0
                    nsum=0
                    tempName=[0]
                    tempSum=[0]
                    newName=[0]
                    newSum=[0]
                    while (not(line[0:6] == "ΣΥΝΟΛΟ")) or (line[0:6] == "------") :
                       proion=cproion(line)
                       if not(proion):      
                            break
                       tempName.append(proion[0])
                       tempSum.append(round(proion[3],2))
                       counter+=1
                       sunolo+=proion[3]
                       line = file.readline()
                    if(line[0:6] == "ΣΥΝΟΛΟ"):
                   
                        line=" ".join(line.split())
                        sun=float(line[8:len(line)])
                        sunolo=round(sunolo,2)
                        if not(sunolo==sun):
                            sun=0
                line = file.readline()
                if line[0:6] == "------"  and afm and proion and  sun:
                    
                    if flag and flagAr:
                        r=first(Node(afm,tempName[1:len(tempName)],tempSum[1:len(tempSum)]))
                        
                        flag=False
                        
                    else:

                        insert(r,Node(afm,tempName[1:len(tempName)],tempSum[1:len(tempSum)]))
                        ekxor+=1
                    continue
            line = file.readline()
            cnt +=1
        inorder(r)
        file.close()
        flagAr=False
        
    elif choice==2:
        tempProd=input("Enter the product name:\t").upper()
        inordersearch(r,tempProd)
    elif choice==3:
        tempAfm=input("Enter Afm:\t")
        print(tempAfm)
        mylist=[("0","0")]
        tempNode=Node(tempAfm,None,None)
        print(tempNode.afm)
        tempNode=search(r,tempNode.afm)
        print("\n")
        print(tempNode.afm)
        for i in range(len(tempNode.product)):
            mylist.append([str(tempNode.product[i]),str(tempNode.total[i])])
        mylist=sorted(mylist,key=lambda x:(x[0]))
        for i in range(1,len(mylist)):    
            print(' '.join(mylist[i]))
    elif choice==4:   
        break
    else :
       continue









