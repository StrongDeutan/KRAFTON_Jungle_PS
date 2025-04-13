import sys
circle_num = int(sys.stdin.readline())
circle_position = [] #start, end
area = 1 + circle_num

for circle_index in range(circle_num):
  center, r = map(int, sys.stdin.readline().split())
  circle_position.append((center - r, center + r))
#원의 양 끝점 => 오른쪽 끝 오름차순, 왼쪽 시작 내림차순

circle_position.sort(key=lambda x: (x[1], -x[0]))
left_stack = [circle_position[0][0]]
right_stack = [circle_position[0][1]]

for circle_index in range(1, circle_num):
  #오른쪽 같으면
  if circle_position[circle_index][1] == right_stack[-1]:
    #스택 길이 확인, 대각선으로 같은지 확인
    if len(right_stack) >= 2 and left_stack[-1] == right_stack[-2]:
      level_down = 0
      while True:
        #스택이 부족하면 종료
        if len(right_stack) < 2+level_down:
          level_down -= 1
          break
        #대각선 값이 다르면 종료
        if left_stack[-1-level_down] != right_stack[-2-level_down]:
          level_down -= 1
          break
        #왼쪽 시작점이 현재 시작점과 같으면 사이에 있는 값 모두 pop한 뒤 영역+1
        if left_stack[-2-level_down] == circle_position[circle_index][0]:
          for pop_num in range(2+level_down):
            left_stack.pop()
            right_stack.pop()
          area += 1
          break
        level_down += 1
    #대각선으로 다르면 Pop
    else:
      left_stack.pop()
      right_stack.pop()
  #왼쪽 같으면 pop
  elif circle_position[circle_index][0] == left_stack[-1]:
    left_stack.pop()
    right_stack.pop()

  left_stack.append(circle_position[circle_index][0])
  right_stack.append(circle_position[circle_index][1])
  
print(area)