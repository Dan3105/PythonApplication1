
import DataScript.DataSp as ds


## Các ví dụ nằm ở file này
if __name__ == '__main__':

    #region Tester
    ##Xử lý các đầu input
    #doc1 = "I did enact Julius Caesar: I was killed in the Capitol; Brutus killed me"
    #doc1ID = "ID1"
    #doc2 = "So let it be with Caesar. The noble Brutus hath told you Caesar was ambitious"
    #doc2ID = "ID2"

    #doc1 = al.TokenizeProcess(doc1)
    #doc2 = al.TokenizeProcess(doc2)

    #pair1 = al.pair(doc1ID, doc1)
    #pair2 = al.pair(doc2ID, doc2)
    
    ##====================================
    #seeResult = al.BuildIndex(al.BuildSortedList(pair1, pair2)) # dạng input đã qua xử lý
    
    ##Figure 1.6
    #print(*al.Intersect(seeResult["caesar"], seeResult["was"]))

    ##Figure 1.7
    #print(*al.IntersecMultiple(seeResult, "caesar", "was", "the"))

    ##Figure 2.10
    #print(al.IntersectWithSkip(seeResult["capitol"], seeResult["i"]))

    ##Figure 2.12
    #pam1 = "pong po pong pi pip pi ha pa pl pu"
    #pam2 = "po po pi ha pa pl pu pu pl pa ppg pong pi"

    #pair1 = al.PairIDList("ID1", pam1.split())
    #pair2 = al.PairIDList("ID2", pam2.split())

    #result = al.GenerateDicTerm([pair1, pair2])

    #print(al.PositionalIntersec(result["pi"], result["pa"], 3))
    
    ##figure 3.5
    #print(al.edit_distance("dam", "cc"))
    #endregion
    #region Halu
    #Data Main
    
    doc1 = "I did enact Julius Caesar: I was killed in the Capitol; Brutus killed me"
    doc1ID = "ID1"

    dataDoc1 = ds.Document(doc1ID, doc1);

    doc2 = "So let it be with Caesar. The noble Brutus hath told you Caesar was ambitious"
    doc2ID = "ID2"
    
    dataDoc2 = ds.Document(doc2ID, doc2);

    doc3 = "Julius Caesar: I was killed in the Capitol; it be with Caesar. The noble Brutus hath told"
    doc3ID = "ID3"

    dataDoc3 = ds.Document(doc3ID, doc3);

    mainData = ds.DocumentDatas([dataDoc1, dataDoc2, dataDoc3])
    #Can than input dau vao
    #figure 1.6
    print(ds.al.Intersect(mainData.GetBuildIndex()["brutus"], mainData.GetBuildIndex()["i"]))

    #figure 1.7
    print(ds.al.IntersecMultiple(mainData, "so", "i", "brutus"))

    #Figure 2.10
    print(ds.al.IntersectWithSkip(mainData.GetBuildIndex()["brutus"], mainData.GetBuildIndex()["noble"]))

    #Figure 2.12
    print(ds.al.PositionalIntersec(mainData.GetDictTerm()["hath"], mainData.GetDictTerm()["told"]))
    #endregion