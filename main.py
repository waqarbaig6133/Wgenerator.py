def solution(s):
  if s < 3:
    print('W cannot be shorter than 3 lines')
  else:
    for x in range(s):
      if x == 0:
        print('*' + (4*s-5-2)*' '+'*')
      elif x ==1:
        print(' '  +  '*'  +  int((4*s-5-4)/2)*' '  +  '*'  + int((4*s-5-4)/2)*' '  + '*')
      elif x == s-1:
        print(x*' '+'*'+(2*s-5)*' '+'*')
      else:
        print((x)*' ' + '*'+ (int(-2*x + 2*s - 3)*' '  +  '*') + (int(2*x-3)*' '  +  '*' +int(-2*x + 2*s - 3)*' '  +  '*') )


solution(7) 
