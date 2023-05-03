# 문제 설명
# park	routes	result
# ["OSO","OOO","OOO"]	["E 2","S 2","W 1"]	[2,1]
# 입출력 예 #1
# 입력된 명령대로 동쪽으로 2칸, 남쪽으로 2칸, 서쪽으로 1칸 이동하면 [0,0] -> [0,2] -> [2,2] -> [2,1]이 됩니다.

''' 정형화되어있다. 여러번 풀어보고 규칙 찾기
1. 이중 배열로 grid 표현하기
2. dirs = {"N":(-1,0), "S":(1,0), "E":(0,1), "W":(0,-1)}
    방향에 따른 row, col를 미리 저장하면 편리하다.
3. new_row, new_col = curr_row + dir_row * offset, curr_col + dir_col * offset
    검사는 new_ 사용하기. curr_는 함부로 바꾸지 않는다.
4. loop와 offset 이용해서 쭈욱 이동하는거 확인해준다.
'''

def solution(park, routes):
    # 1 = 장애물
    # 0 = 이동가능
    row, col = len(park), len(park[0])
    grid = [[0 for c_idx in range(col)] for r_idx in range(row)] # grid에 전부 0이라고 표시시
    curr_row, curr_col = 0, 0 # start point
    
    # 입력을 grid에 옮겨주기
    for r_idx in range(row):
        for c_idx in range(col):
            if park[r_idx][c_idx] == "X": # 장애물
                grid[r_idx][c_idx] = 1
            elif park[r_idx][c_idx] == "S": # 이동가능, 0은 위에서 설정해줌
                curr_row, curr_col = r_idx, c_idx
                
    # 방향과 크기 나누기
    dirs = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    
    # 방향
    for route in routes:
        direction, distance = route.split() # E 2 -> 방향과 칸을 split하기
        dir_row, dir_col = dirs[direction] #(0,1)
        
        is_valid = True # 디폴트 값
        
        # 크기는 offset으로 설정
        for offset in range(1,int(distance)+1):
            # 새롭게 이동한 곳 = 현재 위치 + 방향 * 이동 칸 수
            new_row, new_col = curr_row + dir_row * offset, curr_col + dir_col * offset
            
            if new_row in range(row) and new_col in range(col) and grid[new_row][new_col] == 0:
                # 새롭게 이동한 곳이 바운더리 안에 존재하고 장애물을 만나지 않을 때.
                pass
            
            else:
                is_valid = False # 바운더리를 벗어나거나 장애물을 만났을 때 is_value를 False로 바꾸고 stop
                break
        
        if is_valid: # True 일 때
            curr_row, curr_col = new_row, new_col
            # is_valid = False면 업데이트 안하고, True면 업데이트
            
    # return [curr_row, curr_col]
    print(curr_row, curr_col)
          
park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
solution(park, routes)
            
    
