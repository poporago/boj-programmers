rule = {"up":[0,1] , "down": [0,-1], "left" : [-1,0], "right" : [1,0]}

def solution(keyinput, board):
    answer = [0,0]
    limit = [0,0]
    limit[0] , limit[1] = int((board[0]-1)/2) , int((board[1]-1)/2)
    
    for key in keyinput : 
        new_answer = [answer[0] + rule[key][0]  , answer[1] + rule[key][1] ]
        
        #유효성 검사, 이동후 체크 한뒤 맞으면 할당
        if abs(new_answer[0])<=limit[0] and abs(new_answer[1])<=limit[1] :
            answer = new_answer
            
    
    return answer