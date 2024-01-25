

MIN = -1000
MAX = 1000

class CompactList:
    
    # For the constructor I will use a sorted doubly linked list (see below the classes)
    def __init__(self,inlist=[]):
        
     
        # Sorted list that sorts the input
        self.sorted_list = SortedList()

        # Sorted compact list
        self.compact_list = SortedList()
        
        # Length of the compact list
        self.len = len(self.compact_list)  

        if len(inlist) == 1:
            self.compact_list.insert2(inlist[0])
            self.compact_list.insert2(inlist[0] + 1)
            self.len = len(self.compact_list) 
            
        # Not empty list
        elif inlist != []:

            # Populates sorted linked list
            for i in inlist:
                self.sorted_list.insert2(i)

            # Starts to create the compact list by checking whether the numbers are consecutive or not   
            node = self.sorted_list.head
            start_val = node.item

            while node.next:
                # Checks if the next item (already sorted) is consecutive
                if node.item + 1 == node.next.item:
                    node = node.next

                    # In case it is the last node 
                    if not node.next:
                        final_val = node.item + 1
                        self.compact_list.insert2(start_val)
                        self.compact_list.insert2(final_val)  
                        self.len = len(self.compact_list)

                # If the next item is not consecutive it adds the (compacted) values to the compact list
                else:
                    final_val = node.item + 1
                    self.compact_list.insert2(start_val)
                    self.compact_list.insert2(final_val)
                    
                    start_val = node.next.item
                    node = node.next
                    # In case it is the last node
                    if not node.next:
                        self.compact_list.insert2(start_val)
                        self.compact_list.insert2(start_val + 1) 
                        self.len = len(self.compact_list)
        self.sorted_list = None

    def cardinality(self):
        if self.isEmpty():
            return 0
        else:
            node = self.compact_list.head
            cardinality = 0
            # When the list is length 2 or less
            if not node.next.next:
                cardinality = (node.next.item - node.item)

            # Sums the cardinality in steps of two nodes e.g., consider the compact list [x1, x2, x3, x4] then this sums 
            # (x2 - x1) first and then it sums (x4 - x3). It will therefore give: cardinality = (x2 - x1) + (x4 - x3).
            # Always positive values because they are sorted.
            while node.next.next:
                cardinality += (node.next.item - node.item)
                node = node.next.next
                if not node.next.next:
                    cardinality += (node.next.item - node.item)
        return cardinality

    
    def insert(self,value):
        # If list is empty 
        if self.isEmpty():
            
            head = Node(value, None, None)
            self.compact_list.head = head

            next_n = Node(value + 1, head, None) 
            self.compact_list.head.next = next_n
            self.len = 2
            
        # The union of the value itself and the compact list 
        else:
            if not self.contains(value):
                cl = CompactList([])
                head = Node(value, None, None)
                cl.compact_list.head = head
                next_n = Node(value + 1, head, None)
                cl.compact_list.head.next = next_n
                cl.compact_list.tail = next_n
                cl.len = 2
                
                new_list = self.union(cl)

                self.compact_list = new_list.compact_list
                self.len = len(self.compact_list)
        
    def delete(self,value):
        # The intersection of the complement of the value itself and the original compact_list
        if not self.isEmpty():
            if self.contains(value):
                
                prev_ = self.compact_list
                len_prev = self.len

                cl = CompactList([])
                head = Node(value, None, None)
                cl.compact_list.head = head
                next_n = Node(value + 1, head, None)
                cl.compact_list.head.next = next_n
                cl.compact_list.tail = next_n
                cl.len = 2               

                self.compact_list = cl.compact_list
                self.len = cl.len               
                complement = self.complement()                
                
                self.compact_list = prev_
                self.len = len_prev

                result = self.intersection(complement)

                
                self.compact_list = result.compact_list
                self.len = len(self.compact_list)

    def contains(self,value):
        contained = False
        if self.isEmpty():
            return contained
        else:
            node = self.compact_list.head.next
            counter = 0
            while counter < self.len and not contained:
                if node.prev.item <= value and value < node.item:
                    contained = True
                else:
                    counter += 2
                    if counter < self.len:
                        node = node.next.next                    
        return contained
    
    def subsetOf(self,cl):
        # The empty set is a subset of every set
        if self.isEmpty():
            return True
        # If the cardinality of the union is the same as the cardinality of cl, then true
        else:

            prev_ = self.compact_list
            prev_len = len(self.compact_list)

            union_l = self.union(cl)
            self.compact_list = union_l.compact_list
            self.len = len(self.compact_list)            
            n_union = self.cardinality()           
            

            self.compact_list = cl.compact_list
            self.len = len(self.compact_list)
            n1 = self.cardinality()
            
            self.compact_list = prev_
            self.len = prev_len            
            n2 = self.cardinality()
            
            if n1 == n_union:
                return True
            else:
                return False
            
                        
    def equals(self,cl):
        
        # The empty set is a subset of every set
        if self.isEmpty() or cl == []:
            return False
        
        # If the cardinality of the intersection is the same as the cardinality of cl and the cardinality of the list, then true
        else:        
            prev_ = self.compact_list
            prev_len = len(self.compact_list)

            
            n1 = self.cardinality()


            inter_ = self.intersection(cl)
            self.compact_list = inter_.compact_list
            self.len = len(self.compact_list)    
            n2 = self.cardinality()
            
            self.compact_list = cl.compact_list
            self.len = len(self.compact_list)
            n3 = self.cardinality()
            
            self.compact_list = prev_
            self.len = prev_len
            
            if (n2 == n1) and (n2 == n3):
                return True
            else:
                return False
        

    def isEmpty(self):
        # Empty set
        return self.compact_list.head == None
        
    def complement(self):
        result = CompactList()

        
        if self.isEmpty():
            result.compact_list.insert2(MIN)
            result.compact_list.insert2(MAX)
            result.len = 2
            return result   

        # If the compact list cl has odd length, I convert it to even length
        if self.len % 2 != 0:
            self.compact_list.insert2(MAX)
        
        counter = 0
        node = self.compact_list.head
        
        # If the compact list already represents the whole universe
        if node.item == MIN and node.next.item == MAX + 1:
            result = None

           
        elif node.item == MIN:
            # Adds the values in the ends of each compact list
            while node.next != None:
                if counter % 2 != 0:
                    result.compact_list.insert2(node.item)
                elif counter > 0:
                    result.compact_list.insert2(node.item)
                   
                node = node.next
                counter += 1
            if self.compact_list.tail.item != MAX + 1:
                result.compact_list.insert2(MAX + 1) 
        
        else:
            result.compact_list.insert2(MIN)
            while node != None:
                counter += 1
                if counter % 2 != 0:
                    result.compact_list.insert2(node.item)
                else:
                    result.compact_list.insert2(node.item)
                node = node.next
            if self.compact_list.tail.item != MAX + 1:
                result.compact_list.insert2(MAX + 1)

      
        result.len = len(result.compact_list) 
        return result
        
    def union(self,cl):
        upper_right, lower_right = 1, 0
        upper_left, lower_left = 1, 0

        right = cl.compact_list.head
        right_up = cl.compact_list.head.next
        
        
        left = self.compact_list.head
        left_up = self.compact_list.head.next

        min_inter = 0
        intersection = False
        max_inter = 0
        
        
        result = SortedList()
        
        if self.isEmpty():
            return cl
        elif cl.isEmpty():
            return self
        
            
        # If the compact list cl has odd length, I converted to even length
        if cl.len % 2 != 0:
            cl.compact_list.insert2(MAX)
        
        # In this case I consider two numbers that define a subset of each list, therefore I increase by two in each iteration
        while upper_left < self.len and upper_right < cl.len:
            contained = False                   
            # If compact list and cl do not share any integer then just mix the compact lists
            #First case
            if left_up.item < right.item:
                if intersection:
                    result.insert2(min_inter)
                    result.insert2(max_inter)
                    intersection = False
                    
                # Check whether the compact list is already in the result
                if result.tail != None:
                    if result.tail.item < left_up.item:
                        result.insert2(left.item)
                        result.insert2(left_up.item) 

                else:
                    result.insert2(left.item)
                    result.insert2(left_up.item) 

                lower_left += 2
                upper_left += 2   
                if left_up.next:
                    left = left.next.next
                    left_up = left_up.next.next
                    
            # Second case   
            elif right_up.item < left.item:
                if intersection:
                    result.insert2(min_inter)
                    result.insert2(max_inter)                    
                    intersection = False
                    
                # Check wheter the compact list is already in the result
                if result.tail != None:
                    if result.tail.item < right_up.item:
                        result.insert2(right.item)
                        result.insert2(right_up.item)    

                else:
                    result.insert2(right.item)
                    result.insert2(right_up.item)    

                lower_right += 2
                upper_right += 2 
                if right_up.next:
                    right = right.next.next
                    right_up = right_up.next.next
                    
            # If compact list is contained in cl
            elif left_up.item <= right_up.item and left.item >= right.item:
                if intersection:
                    result.insert2(min_inter)
                    result.insert2(max_inter)
                    intersection = False
                lower_left += 2
                upper_left += 2   
                contained = True
                if left_up.next:
                    left = left.next.next
                    left_up = left_up.next.next
                    
            # If cl is contained in compact list
            elif left_up.item >= right_up.item and left.item <= right.item:
                if intersection:
                    result.insert2(min_inter)
                    result.insert2(max_inter)
                    intersection = False                
                lower_right += 2
                upper_right += 2
                contained = True
                if right_up.next:
                    right = right.next.next
                    right_up = right_up.next.next
            # If some part of the lists intersects i.e., if we have x1 < y1 and x2 < y2 for the compact lists [x1, x2] and [y1, y2]
            # Case 1
            elif left.item <= right.item and left_up.item <= right_up.item:
                if not intersection:
                    min_inter = left.item
                intersection = True
                max_inter = right_up.item
                lower_left += 2
                upper_left += 2
                if left_up.next:
                    left = left.next.next
                    left_up = left_up.next.next
            # If some part of the lists intersects i.e., if we have y1 < x1 and y2 < x2 for the compact lists [x1, x2] and [y1, y2]
            # Case 2
            elif right.item <= left.item and right_up.item <= left_up.item:

                if not intersection:
                    min_inter = right.item
                intersection = True
                max_inter = left_up.item
                lower_right += 2
                upper_right += 2
                if right_up.next:
                    right = right.next.next
                    right_up = right_up.next.next
        if intersection:
            result.insert2(min_inter)
            result.insert2(max_inter)
            
            intersection = False
            if upper_left < self.len:
                upper_left += 2
                lower_left += 2
                if left_up.next != None:
                    left = left.next.next
                    left_up = left_up.next.next
            if upper_right < cl.len:
                upper_right += 2
                lower_right += 2
                if right_up.next != None:
                    right = right.next.next
                    right_up = right_up.next.next
                
        # It adds the rest of the lists that was not considered in the while (as in merge)
        # It would be a part of either cl or self.compact_list
        if upper_right <= cl.len and not intersection:
            node = right
            while node:
                result.insert2(node.item)
                node = node.next
        if upper_left <= self.len and not intersection:
            node = left
            while node:
                result.insert2(node.item)
                node = node.next
                
        result_compact = CompactList([])
        result_compact.compact_list = result 
        return result_compact
        
    def intersection(self,cl):
        # Complement of the union of the complement self and the complement of cl
        
        prev_len = self.len
        prev_ = self.compact_list
        
        # Complement of A
        A_c = self.complement()
        
        # Complement of B
        self.compact_list = cl.compact_list
        self.len = cl.len
        B_c = self.complement()

        
        # Linked list of complement of A
        self.compact_list = A_c.compact_list
        self.len = A_c.len

        # Union of complement of A and complement of B
        AUB = self.union(B_c)

        # Linked list for union of complements of A and B
        self.compact_list = AUB.compact_list
        self.len = AUB.len
        
        
        # Complement of the union of complements
        result = self.complement()
        
        
        self.compact_list = prev_
        self.len = prev_len
        
        if AUB.compact_list.head != None:
            if AUB.compact_list.head.item == MIN and AUB.compact_list.head.next.item == (MAX + 1):
                return None
        
        return result

    def difference(self,cl):
        # self \ cl = A intersection B_c
        
        if self.isEmpty() or cl == [] or self.equals(cl) or self.subsetOf(cl):
            return None
        
        
        # Intersection of self and the complement of cl
        else:        
            prev_ = self.compact_list
            prev_len = self.len   
            
            self.compact_list = cl.compact_list
            self.len = cl.len
            cl_c = self.complement()
            
            self.compact_list = prev_
            self.len = prev_len       
            
            
            result = self.intersection(cl_c)
            
            return result
        
    def __str__(self):
        if self.compact_list.head == None:
            return "Empty"
        p = self.compact_list.head
        s = ''
        while p.next.next != None:
            if p.item == p.next.item - 1:
                s += '[' + str(p.item) + ']' + ' U '
            else:
                s += '[' + str(p.item) + ', ' + str( p.next.item - 1) + ']' + ' U '
            p = p.next.next
        s += '[' + str(p.item) + ', ' + str(p.next.item - 1) + ']'
        return s         
        

    
    
################## Sorted linked list from the MA 407 seminars code adapted for the assessed coursework #################
class Node:
    def __init__(self, it, p, n):
        self.item = it
        self.prev = p
        self.next = n

class SortedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # inserts x into list so that list stays sorted
    def insert2(self,x):
        if self.head == None or self.head.item >= x:    # empty list or x to become the first item
            temp = Node(x,None,self.head)
            if self.head != None:
                self.head.prev = temp
            self.head = temp
        else:
            p = self.head
            while p.next != None and p.next.item < x:  # find first value >= x
                p = p.next

            temp = Node(x,p,p.next)    
            if p.next != None:
                p.next.prev = temp
            else:
                self.tail = temp
            p.next = temp  
    
    def __len__(self):
        start = self.head
        n = 0
        while start != None:
            start = start.next
            n += 1
        if self.head == None:
            return 0
        return n    
######################### End of sorted linked list #######################################            
            
    
    
if __name__ == "__main__":

    mycl1 = CompactList([])
    print(mycl1)
    print(mycl1.cardinality())
    
    mycl2 = CompactList([9,8,3,4,5])
    print(mycl2)
    print(mycl2.cardinality())
    print(mycl2, "contains 4:",mycl2.contains(4)) 

    mycl1 = CompactList([10,1,11])
    mycl3 = mycl1.union(mycl2)
    print(mycl3)
    print(mycl3.cardinality())
    
    mycl1 = mycl2.complement()
    print(mycl1)
    print(mycl1.cardinality())

    mycl1 = CompactList([MAX])
    print(mycl1)
    print(mycl1.cardinality())
