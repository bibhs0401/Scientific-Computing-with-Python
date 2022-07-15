def arithmetic_arranger(problems,ans=False):

  if len(problems) > 5:
    return'Error: Too many problems.'

  for i in range(len(problems)):

    #separating numbers and operand
    
    num=problems[i].split()
    
    first_num=num[0]
    second_num=num[2]
    operator=num[1]


    if len(first_num) < 5 and len(second_num) < 5:
      if first_num.isnumeric() and second_num.isnumeric():
        if operator == '+':
          result=str(int(first_num)+int(second_num))
        elif operator =='-':
          result=str(int(first_num)-int(second_num))
        else:
          return 'Error: Operator must be '+' or '-'.'
      else:
        return'Error: Numbers must only contain digits.'
    else:
      return'Error: Numbers cannot be more than four digits.'

    longest_num=first_num if first_num > second_num else second_num
    dash= '-' * (len(longest_num)+2)

    if ans:
      arranged_problems= first_num.rjust(len(dash)) + '\n' + operator +' ' + second_num + '\n' + dash +'\n' 
    else:
      arranged_problems= first_num.rjust(len(dash)) + '\n' + operator +' ' + second_num + '\n' + dash +'\n' + result.rjust(len(dash))+ '\n'
    
  return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49",'2 + 4567']))