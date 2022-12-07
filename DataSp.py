import AlgorithmLib as al


#region Main Data
class Document:

    def __init__(self, documentID : str, ntext : str):
        self.documentID = documentID
        self.__listProcessor = []
        self.__NormalizeString(ntext)
        

    def __NormalizeString(self, ntext : str):
        termList = ntext.split()
        for text in termList:
            self.__listProcessor.append(al.TokenizeProcess(text))
        #[self.__listProcessor.append(text) for text in al.TokenizeProcess(ntext)]


    def GetListProcess(self) -> list:
        return self.__listProcessor.copy()


class DocumentDatas:
    __listDocument = [] #list<Document>
    __dictBuildIndex = {}
    __dictTerm = {}
    #Init
    
    def __init__(self, listContainer = []):
        self.__listDocument = listContainer
        self.__UpdateData()
    
#region attribute
    def GetListDocument(self) -> list:
        return self.__listDocument.copy()

    def GetBuildIndex(self) -> dict:
        return self.__dictBuildIndex.copy()

    def GetDictTerm(self) -> dict:
        return self.__dictTerm.copy()
#endregion

#region Func    
    #Don't use this function too much better use init
    def AddDataDocument(self, document : Document):
        self.__listDocument.append(document)
        self.__UpdateData()
    def __UpdateData(self):
        self.__dictBuildIndex = self.__GenerateBuildIndex()
        self.__dictTerm = self.__GenerateDicTerm()
    
    def __GenerateBuildIndex(self) -> dict:
        return al.BuildIndex(al.BuildSortedList(self.__listDocument))


    def __GenerateDicTerm(self) -> dict:
        return al.GenerateDicTerm(self.__listDocument)
#endregion
#endregion

