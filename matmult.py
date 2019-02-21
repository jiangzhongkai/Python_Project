"""-*- coding: utf-8 -*-
 Author  : Peter_Bonnie
 FileName    : matmul.py
"""
"""
desc:
  main function:Matrix multiplication
  input:two matrixs
  output:result 
"""

def str_list(input_Str):
    """convert string to list"""
    temp=input_Str.split(' ')   #define temp list to save the result
    for i in range(len(temp)):
        temp[i]=float(temp[i])

    return temp

def get_Row_Col(input_Str):
    """get the rows and columns of matrix"""
    rows,columns=input_Str.split(' ')
    return int(rows),int(columns)

if __name__=="__main__":

   """step1：get the rows and columns"""
   import sys
   commandLine=sys.stdin.readlines()

   row_1,col_1=get_Row_Col(commandLine[0].strip('\n'))

   """step2：get the matrix value"""
   temp_a_list=[]   #save value
   temp_b_list=[]
   # temp_row_1=row_1
   for i in range(row_1):
       temp_a_list.append(str_list(commandLine[i+1].strip('\n')))

   row_2,col_2=get_Row_Col(commandLine[row_1+1].strip('\n'))
   for i in range(row_2):
       temp_b_list.append(str_list(commandLine[i+row_1+2].strip('\n')))

   if col_1!=row_2:
       print("invalid input")
   #     exit()
   else:
       mat_c=[[0]*col_2 for i in range(len(temp_a_list))]
       for i in range(row_1):
           for j in range(col_2):
               for k in range(len(temp_b_list)):
                   mat_c[i][j]+=temp_a_list[i][k]*temp_b_list[k][j]

               """step3:output the final result"""
               print(mat_c[i][j])



