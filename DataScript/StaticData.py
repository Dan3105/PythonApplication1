class StaticData:
    def get_id(self): return self.__idChapter
    def get_content(self) : return self.__content

    def __init__(self, idChapter : str, content : str):
        self.__idChapter = idChapter
        self.__content = content
    
class MainData:
    __dictData = {"chapter 1" : "Random world and some awsome thing but too lazy to shooww haha",
                  "chapter 2" : "Hahahaa",
                  "chapter 3" : "BWwaasad sadfklaj s;djklajk lj kdas jk f ;kdjsfkl",
                  "chapter 4" : "Yahy ",
                  "chapter 5" : "Bleh bleh"
                  }
    def get_data_content(self, chapter : str) -> str:
        try:
            return self.__dictData[chapter]
        except:
            return ""

    def get_id_by_index(self, index : int) -> str:
        try:
            return self.__dictData.keys[index]
        except:
            return ""