import math

#====================Các hàm xử lý input===================
#@me :>
#
class Pair:
    def __init__(self, _first, _second):
        self.first = _first
        self.second = _second

#việc sàng lọc, tìm kiếm chuỗi không bị ảnh hưởng bởi 
#in hoa, in thường và các dấu đặc biệt (vd: line tương đương với @line;')
def TokenizeProcess(txt : str):
    txt = txt.lower()
    for char in txt:
        if not char.isalpha() and not char == ' ':
            txt = txt.replace(char, '')
    return txt

# Objective: Gộp tất cả các phần tử có trong class Document và sort theo
# từ (alphabet) nếu từ giống nhau sort theo ID
# *pairListParagraph: tập các class pair chứa ID đoạn văn và đoan văn

def BuildSortedList(pairListParagraph : list):
    try: 
       listCombine = []
      
       for paraType in pairListParagraph:
        [listCombine.append([term, paraType.documentID]) for term in paraType.GetListProcess()]

       listCombine.sort(key = lambda x : (x[0], x[1]))
       
       return listCombine
    except Exception as e:
        print(e)
        return None
    #finally:

##
#Struct of Figure1.4
#Không có struct này thì có cl làm được 2 bài dưới :D
# BuildSortedList() -> list: cần xử lý qua hàm này trước 
#{term: postingList (List of ID <=> sortedList)[]}
###        
def BuildIndex(listCombine : list) -> dict:
    try:
        INDEX_TERM = 0
        INDEX_DOCID = 1
        dictionary = {}
        
        for element in listCombine:
            if dictionary.get(element[INDEX_TERM]) == None:
                setOfPosting = {element[INDEX_DOCID]}
                dictionary[element[INDEX_TERM]] = setOfPosting #setType
            else:
                dictionary[element[INDEX_TERM]].add(element[INDEX_DOCID])
        
        # sắp xếp lại dựa theo id
        for key, value in dictionary.items():
            dictionary[key] = sorted(value)
        
        return dictionary
    except Exception as e:
        print(e)
        return None
##=======================================================##







#@Mrs Thanh Thảo :>
#Intersect algorithm 1.6
#   @dictTerm1 = value trong dict {key: term, value: posting list} term: tu can tim
#   @dictTerm2 = value trong dict {key: term, value: posting list} term: tu can tim
# Hướng đi thuật toán:
# 
# 
#
#
#return: tập các chương mà 2 từ đưa vào CÙNG tồn tại
#
def Intersect(term1 : list, term2 : list) -> list:
    #term1 = TokenizeProcess(term1)
    #term2 = TokenizeProcess(term2)
    listOfIntersect = []
    try:
        startIndex1 = 0
        #listPostID1 = list(mainData.GetBuildIndex()[term1])

        startIndex2 = 0
        #listPostID2 = list(mainData.GetBuildIndex()[term2]) 

        while startIndex1 < len(term1) and startIndex2 < len(term2):
            if term1[startIndex1] == term2[startIndex2]:
                listOfIntersect.append(term1[startIndex1])
                startIndex1 += 1
                startIndex2 += 1
            elif term1[startIndex1] < term2[startIndex2]:
                startIndex1 += 1
            else:
                startIndex2 += 1
    except Exception as e:
        print(e)
    finally:
        return listOfIntersect


#Figure 1.7 @me :>
#   @dictData: dict chua data: dict {key: term, value: posting list}
#   @*searchTermsQuerries: list of terms
#   return tập các chương có cùng tồn tại các từ có trong querry
#
def IntersecMultiple(mainData : type, *searchTermsQuerries):
    result = []
    #xu ly cac chuoi trong searchTerms
    listTextNormalize = [TokenizeProcess(text) for text in searchTermsQuerries]
    # list contain values that match with searchTerm
    handleData = [Pair(element, mainData.GetBuildIndex()[element]) for element in listTextNormalize if mainData.GetBuildIndex().get(element) != None]
    terms = [t for t in sorted(handleData, key = lambda x : len(x.second), reverse = True)]

    try:
        result = terms[0].second
        terms = terms[1:]

        while len(terms) > 0:
            result = Intersect(result, terms[0].second);
            terms = terms[1:]
    #print(handleData)
    except Exception as e:
        print(e)
    finally:
        return result

#-----------------------Figure 2.10----------------------------
#@Mr. Danh:
# Create Skip List
# this skip for now use index to check
# tạm thời chưa có linked list
#Data Struct
class Node:
    def __init__(self, dataNode = None):
        self.dataNode = dataNode
        self.nextNode = None

class LinkedList:
    def __init__(self, node : Node = None):
        self.head = node

    def append(self, nextNode : Node = None):
        if self.head == None:
            self.head = nextNode
            return

        copier = self.head
        while copier.nextNode != None:
            copier = copier.nextNode
    
        copier.nextNode = nextNode

    def GetHeadData(self):
        if self.head != None:
            return self.head.dataNode
        return None

    def skip(self):
        if self.head != None:
            self.head = self.head.nextNode
        return self
          
    def canSkip(self):
        return self.head.nextNode != None
   
def GenerateSkipList(p) -> LinkedList:
    result = LinkedList(Node(0))
    try:
        #print(*p, end = '\n')
        #this gonna be len of result
        spaceSkip = round(math.sqrt(len(p)))
        #add the stater
        #result.append(0) 

        for i in range(1, spaceSkip):
            result.append(Node(result.GetHeadData() + spaceSkip))

    except Exception as e:
        print(e)
    finally:
        return result

#def skip(p):
#    p = p[1:]
#    return p
#def hasSkip(p):
#    return len(p) > 1
#Algorithm 2.10
#Hướng đi thuật toán:
#
#
#
#
#
def IntersectWithSkip(dictTerm1, dictTerm2):
    answer = []
    try:
        startIndex1 = 0
        listPostID1 = list(dictTerm1.copy())
        skipPointer1 = GenerateSkipList(listPostID1)

        startIndex2 = 0
        listPostID2 = list(dictTerm2.copy()) 
        skipPointer2 = GenerateSkipList(listPostID2)

        while startIndex1 < len(listPostID1) and startIndex2 < len(listPostID2):
            if listPostID1[startIndex1] == listPostID2[startIndex2]:
                answer.append(listPostID1[startIndex1])
                startIndex1+=1
                startIndex2+=1
            elif listPostID1[startIndex1] < listPostID2[startIndex2]:
                if skipPointer1.canSkip() and listPostID1[skipPointer1.GetHeadData()] <= listPostID2[startIndex2]:
                    while skipPointer1.canSkip() and listPostID1[skipPointer1.GetHeadData()] <= listPostID2[startIndex2]:
                        startIndex1 = skipPointer1.skip().GetHeadData()
                else:
                    startIndex1 += 1
            else:
                if skipPointer2.canSkip() and listPostID2[skipPointer2.GetHeadData()] <= listPostID1[startIndex1]:
                    while skipPointer2.canSkip() and listPostID2[skipPointer2.GetHeadData()] <= listPostID1[startIndex1]:
                        startIndex2 = skipPointer2.skip().GetHeadData()
                else:
                    startIndex2 += 1
    except Exception as e:
        print(e)
        
    finally:
        return answer

#======================================End Figure 2.10==============================

#==============================Figure 2.12==================================


#return index of ID found
def FindSatisfied(listArr : list, needID : int) -> int:
    for i in range(0, len(listArr)):
        if listArr[i].first == needID:
            return i
    else:
        return -1

#@listOfParagraph: [PairIDList<id, array>]
def GenerateDicTerm(listOfParagraph : list) -> dict:
    result = {}
    #Example of return type
    #result = {
    #       "term" : 
    #       "info" : 
    #       {
    #           [
    #               Pair<pairID, [position that "term" appear]>
    #               Pair<pairID, []>
    #               Pair<pairID, []>
    #           ]
    #       }
    #}
    try:
        for document in listOfParagraph: #Document : idDoc, listProcessor
            listProcess = document.GetListProcess()
            for i in range(0, len(listProcess)):
                if result.get(listProcess[i]) == None:
                    result[listProcess[i]] = {"info" : []}
                finder = FindSatisfied(result[listProcess[i]]["info"], document.documentID)
                #print(finder)
                if finder == -1:
                    result[listProcess[i]]["info"].append(Pair(document.documentID, []))
                    finder = len(result[listProcess[i]]["info"]) - 1
    
                result[listProcess[i]]["info"][finder].second.append(i)
                
    except Exception as e:
        print(e)
    finally:
        return result

#
#Hướng đi thuật toán:
#
##
def PositionalIntersec(p1, p2, k = 1) -> list:
    answer = []
    try:
        index1 = 0
        index2 = 0

        data_list_p1 = p1["info"]   
        data_list_p2 = p2["info"]
    
        while index1 < len(data_list_p1) and index2 < len(data_list_p2):
            doc_id_1 = data_list_p1[index1].first
            doc_id_2 = data_list_p2[index2].first
            if doc_id_1 == doc_id_2:
                l = []
                pp1 = data_list_p1[index1].second
                pp2 = data_list_p2[index2].second
                indexP1 = 0

                while indexP1 < len(pp1):
                    indexP2 = 0
                    while indexP2 < len(pp2):
                        if abs(pp1[indexP1] - pp2[indexP2]) <= k:
                            l.append(indexP2)
                        elif pp2[indexP2] > pp1[indexP1]:
                            break
                        indexP2 += 1
                    for item in l:
                        if abs(pp2[item] - pp1[indexP1]) > k:
                            l.remove(item)
                    for ps in l:
                        answer.append({"document_id" : doc_id_1, "positional_data_1" : pp1[indexP1], "positional_data_2" : pp2[item]})
                    indexP1 += 1
                index1 += 1
                index2 += 1
            elif doc_id_1 < doc_id_2:
                index1 += 1
            else:
                index2 += 1
    except Exception as e:
        print(e)
        #print(e.with_traceback())
    finally:
        return answer

#====================end Figure 2.12

#Mrs. Thích đấm tui  ):<
#Hướng đi thuật toán:
#
#
#
#
#
#
def edit_distance(s1 : str, s2 : str) -> int:
    # s1 and s2 are strings
    # returns the edit distance between s1 and s2

    # initialize the matrix
    m = len(s1) + 1    # number of rows
    n = len(s2) + 1   # number of columns
    # initialize the matrix to all zeros
    D = [[0 for j in range(n)] for i in range(m)]

    # initialize the first row and column
    for i in range(m):  # for each row
        D[i][0] = i    # set the first column to 0, 1, 2, 3, ...
    for j in range(n):  # for each column
        D[0][j] = j   # set the first row to 0, 1, 2, 3, ...

    # fill in the rest of the matrix
    for i in range(1, m):   # for each row
        for j in range(1, n):   # for each column
            if s1[i-1] == s2[j-1]:  # if the characters match
                # copy the value from the upper left diagonal
                D[i][j] = D[i-1][j-1]
            else:
                # take the minimum of the three values above and add 1
                D[i][j] = min(D[i-1][j], D[i][j-1], D[i-1][j-1]) + 1

    # return the edit distance
    return D[m-1][n-1]




