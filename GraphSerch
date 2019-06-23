from collections import deque

friends = {}
friends["me"] = ["Aaa","Bbb","Ccc"] 
friends["Aaa"] = ["Ddd", "Eee",]
friends["Bbb"] = ["Eee"]
friends["Ccc"] = ["Fff"]
friends["Ddd"] = []
friends["Eee"] = []
friends["Fff"] = []

def isStudent(person):
    student = ["Fff"]
    if person in student:
        return True
        
def search(people):
    search_queue = deque()
    search_queue += friends[people]
    searched = []
    while search_queue:
        name = search_queue.popleft()
        if name not in searched:
            if isStudent(name):
                print(name, "is student")
                return True
            else:
                #print(name, "is not student")
                search_queue += friends[name]
                #print("SQ",search_queue)
                searched.append(name)
    return False
    
search("me")
            
    
