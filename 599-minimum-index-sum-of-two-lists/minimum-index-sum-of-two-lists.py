class Solution(object):
    def findRestaurant(self, list1, list2):
        index_map={}
        for i , name in enumerate(list1):
            index_map[name]=i
        min_sum=float('inf')
        resultat=[]
        for j , name in enumerate(list2):
            if name in index_map:
                index_sum=index_map[name]+j
                if index_sum<min_sum:
                    min_sum=index_sum
                    resultat=[name]
                elif index_sum==min_sum:
                    resultat.append(name)
        return resultat  

            
                
