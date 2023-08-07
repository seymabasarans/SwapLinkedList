class Node:
  # Creating a node
  def __init__(self, data): #constructor
    self.data = data
    self.next = None
    
class swapNodes:
    def __init__(self): #constructor
        self.head = None 

    def searchNodes(self, n1, n2): #değiştirmek istenen buluyoruz
        node1 = node2 = self.head #hepsi listenin başı yaptık
        #işaretçilerle listeyi dolaşıcaz
        prevn1 = prevn2 = None #Bunlar x ve y değerlerini içeren düğümleri bulduktan sonra bu düğümlerin önceki düğümlerini tutmak için
        
        # search for x 
        #döngü currentX.data eşit olana veya currentX işaretçisi boş (None) olana kadar devam eder
        while node1.data != n1 and node1 != None:
            prevn1 = node1
            node1 = node1.next

        # search for y
        while node2.data != n2 and node2 != None:
            prevn2 = node2
            node2 = node2.next
              
        return prevn1, node1, prevn2, node2, 

    def sortList(self):  
        #Node current will point to head  
        current = self.head;  
        index = None;  
          
        if(self.head == None):  
            return;  
        else:  #düğümleri sıralamak için Bubble Sort algoritmasını uyguluyoruz
            while(current != None):  
                 
                index = current.next;  #index düğümünü, current düğümünden son düğüme kadar dolaşır
                  
                while(index != None):  
                    #If current node's data is greater than index's node data, swap the data between them  
                    if(current.data > index.data):  
                        temp = current.data;  
                        current.data = index.data;  
                        index.data = temp;  
                    index = index.next;  
                current = current.next;  
    #elemanları küçükten büyüğe sıralarız
 
      
    def swapNode(node1, node2):
        temp = node1.data
        node1.data = node2.data
        node2.data = temp
        
    def rangeSwap(self, start, end): 
        if start == end: 
            return 
        prevstart, nodestart, prevend, nodeend = self.searchNodes(start, end)
        
        if nodestart is None or nodeend is None:
            return
        
        while nodestart != nodeend: 
            self.swapNodes(nodestart,nodeend)
            nodestart=nodestart.next
            nodeend=nodeend.next
                
        
            
    
        
    def swap(self, n1, n2):
        
         # both keys are same do nothing
        if n1 == n2:
            return
    
        prevn1, node1, prevn2, node2 = self.searchNodes(n1, n2)
        #ilk aradığımız verileri buluyoruz
        
        if node1 is None and node2 is None: #n1 n2 yoksa
             return
            
        # x is not head
        if  prevn1 is not None: #n1 değeri baş düğüm değilse
              prevn1.next = node2 #düğümünün "next" işaretçisini node2 düğümüne bağlarız prevn1 düğümü n1 değerini içeren düğümün ardından gelir.
        else:
            # make y as head
            self.head = node2 
    
        # y is not head
        if  prevn2 is not None:
              prevn2.next = node1  
        else:
            # make x as head
            self.head = node1 
    
        # swap pointers 
        
        temp = node1.next
        node1.next = node2.next #node1 düğümü,node2 düğümünden sonraki düğümü işaret eder.
        node2.next = temp
  
    def addNode(self, new_data):
        new_node = Node(new_data)
        #new_data değerini içeren yeni bir düğüm oluşturuyoruz, new_node artık bağlı listeye ekleyeceğimiz yeni düğümü temsil ediyor.
        new_node.next = self.head #(new_node.next) bağlı listenin mevcut baş düğümü olan self.head'e bağlıyoruz.
        self.head = new_node ##listenin baş düğümü
 
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="")
            temp = temp.next
            if temp is not None:  # Son elemandan sonra virgülü koymamak için
               print(" , ", end="")   
               
llist=swapNodes()

llist.addNode(6)  
llist.addNode(7)  
llist.addNode(4)  
llist.addNode(8)
llist.addNode(1)
llist.addNode(3)
llist.addNode(2)
llist.addNode(5) 

print('Before: ')
llist.printLinkedList()
  
llist.sortList()
  
llist.swap(4, 5) 

llist.swap(7,8)

print('\nAfter: ')
#llist.printLinkedList()                 

llist.rangeSwap(1,5)