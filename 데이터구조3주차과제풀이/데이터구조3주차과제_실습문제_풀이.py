# 라인에디터

#리스트 구현(클래스)
class ArrayList:		  
    def __init__( self ):
        self.items = []

    def insert(self, pos, elem) :
        self.items.insert(pos, elem)
    def delete(self, pos) :
        self.items.pop(pos)
    def isEmpty( self ):
        return self.size() == 0
    def getEntry(self, pos) :
        return self.items[pos]
    def size( self ):
        return len(self.items)
    def clear( self ) :
        self.items = []	
    def find(self, item) :
        return self.items.index(item)
    def replace(self, pos, elem) :
        self.items[pos] = elem
    def sort(self) :
        self.items.sort()
    def merge(self, lst) :
        self.items.extend(lst)
    def display(self, msg='ArrayList:' ):
        print(msg, self.size(), self.items)

def myLineEditor() :	
    list = ArrayList()
    filename=""
    while True :
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, f-검색, l-파일읽기, s-저장, q-종료=> ")
        if command == 'i' :		
            pos = int( input("  입력행 번호: "))
            str = input("  입력행 내용: ")	    
            list.insert(pos, str)		
        elif command == 'd' :			
            pos = int( input("  삭제행 번호: "))
            list.delete(pos)			
        elif command == 'r' :			
            pos = int( input("  변경행 번호: "))
            str = input("  변경행 내용: ")	    
            list.replace(pos, str)		        
        elif command == 'q' : return	        
        elif command == 'p' :		            
            print('Line Editor')
            for line in range (list.size()) :   
                print('[%2d] '%line, end='')    
                print(list.getEntry(line))      
            print()
        elif command == 'f' :		
            keyword=input("검색 문자열 : ")
            for line in range(list.size()):
                str=list.getEntry(line)
                if keyword in str:
                    print('[%2d] '%line, end='')    
                    print(str)            
        elif command == 'l' :
            filename=input("파일 이름 : ")
            infile = open(filename , "r")       
            lines = infile.readlines()	        
            for line in lines:		            
                list.insert(list.size(), line.rstrip('\n'))
            infile.close()			
        elif command == 's' :		
            filename=input("파일 이름 : ")
            outfile = open(filename , "w")
            for i in range(list.size()) :
                outfile.write(list.getEntry(i)+'\n')
            outfile.close()

myLineEditor()

