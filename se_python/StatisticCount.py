import numpy as np
import csv
import pandas as pd
from pandas.core.frame import DataFrame
import json
import time
import math
import collections
# import sklearn
from sklearn.neural_network import MLPClassifier,MLPRegressor
#show all the info when using pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 5000)
# Recond_txtFilePath = "../Tarantula_00_robert/recond.txt"

# 选择testcase： mid， bubble
TEST_BUBBLE = True
# TEST_BUBBLE = False

# TEST_MID = True
TEST_MID = False

# EST_MID = True if TEST_BUBBLE==False else False
if not (TEST_BUBBLE ^ TEST_MID) :
    raise Exception("Own_Exception-Function Failed:TEST_BUBBLE and TEST_MID Error")

if TEST_BUBBLE:
    testcase_PATH = "BubbleSort/"
elif TEST_MID:
    # testcase_PATH = "../Tarantula_00_robert/recond.txt"
    testcase_PATH = "Tarantula_00_robert/"
else:
    pass


def ActualMid(x,y,z):
    print("\nIn function ActualMid\n")
    actual_recond = open("actual_recond.txt", "w+")
    count = 0
    time.time()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,file=actual_recond)
    for i in range(1,x+1):
        for j in range(1, y+1):
            for k in range(1, z+1):
                # if( i == j):
                #     continue
                # if( i == k):
                #     continue
                # if( j == k):
                #     continue

                count +=1
                list = [i,j,k]
                list.sort()
                mid = list[1]
                # print("{:d}".format(count))
                print(" {:2d} {:2d} {:2d} Mid={:2d}".format(i,j,k,mid),file=actual_recond)

    print("len:",len(actual_recond.readlines()))
    actual_recond.close()

def ActualBubble(x,y,z,m):
    print("\nIn function Bubble\n")
    actual_recond = open("actual_recond.txt", "w+")
    count = 0
    time.time()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,file=actual_recond)
    for i in range(1,x+1):
        for j in range(1, y+1):
            for k in range(1, z+1):
                for l in range(1, m+1):
                # if( i == j):
                #     continue
                # if( i == k):
                #     continue
                # if( j == k):
                #     continue

                    count +=1
                    list1 = [i, j, k, l]
                    list1.sort()

                    # mid = list[1]
                    # print("{:d}".format(count))
                    # print("INPUT:{:d} {:d} {:d} {:d}".format(i, j, k, l),file=actual_recond)
                    # print("Sorted: ",list1,file=actual_recond)
                    print("INPUT:", i, " ", j, " ", k, " ", l,
                          " Sorted:", list1[0], " ", list1[1], " ", list1[2], " ", list1[3], " ",
                          file=actual_recond,sep='')


    print("len:",len(actual_recond.readlines()))
    actual_recond.close()

def GetTestCaseNumber(): #获得testcase的个数
    # print("\nIn function GetTestCaseNumber\n")
    # f = open("../Tarantula_00_robert/recond.txt")
    f = open("../" + testcase_PATH + "recond.txt")
    lines = len(f.readlines())
    print("There are %d lines in %s" % (lines, f))
    f.close()
    return (lines)

linedata_without_statement = []
linedata = [] #testcase * statement  的矩阵
TestCaseFilename = []
# ProgramFilename = "../Tarantula_00_robert/test"
ProgramFilename =  "../" + testcase_PATH + "test"

'''=========creat test.csv file name-path=============='''
def ProcessTestCaseFilename(filenumber): #批量处理的文件名 路径+文件名
    # print("\nIn function ProcessTestCaseFilename\n")
    for i in range(1,filenumber):
        # filename1 = "../Tarantula_00_robert/test"
        filename1 =  ProgramFilename
        filename2 = str(i)
        filename3 = ".csv"
        # filename3 = ".json"
        # print(filename1 + filename2 + filename3)
        TestCaseFilename.append(filename1 + filename2 + filename3)
    # print(TestCaseFilename, '\nlen of TestCaseFilename',len(TestCaseFilename))
    total_file_number = len(TestCaseFilename)
    print("total_file_number={:d}\n".format(total_file_number))
    return TestCaseFilename, total_file_number


#filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
#这个函数最后出来的是testcase*statement的矩阵
def ProcessOneCsv(TestCaseFilename):
    # print("ProcessOneCsv")
    row = []
    row_split = []
    row_split_without_statemanet = []
    df = pd.read_csv(TestCaseFilename, header=None, sep=' ')
    j = 0
    statement_number = len(df)
    # print("statement_number=",statement_number)
    # print("df=",df)
    for i in range(0,statement_number):
        row.append((df[0][i]))
        # print(i, df[0][i])
        if TEST_MID == True:        
            if((i > 5) & (23 > i)):
                temp = (row[i].split(','))
                row_split.append(temp)
                # print("j=",j,temp[1])
                row_split_without_statemanet.append(temp[1])

                # print(np.array(row_split).shape,np.array(row_split)[j][1])
                j = j + 1
        elif TEST_BUBBLE == True:
            if((i > 7) & (29 > i)):
                temp = (row[i].split(','))
                row_split.append(temp)
                # print("j=",j,temp[1])
                row_split_without_statemanet.append(temp[1])

                # print(np.array(row_split).shape,np.array(row_split)[j][1])
                j = j + 1
        else:
            pass

            # temp = str(temp)
            # row_split.append(temp.split(','))
    # print(row_split)
    # print('Test row:',row)
    # print(row_split,'\n',np.array(row_split).shape)#charge to array aim to kown the shape of list
    # print(row_split[1][1],type(row_split[1][1]))
    # linedata_without_statement.append()
    linedata.append(row_split)
    linedata_without_statement.append(row_split_without_statemanet)
    # return  row_split #这个函数最后出来的是testcase*statement的矩阵
    # return statement_number

# def PcocessStr2IntForLineDataWithoutStatement():
def PcocessStr2IntForLineDataWithoutStatement(number):
    print("PcocessStr2IntForLineDataWithoutStatement\n shape:",np.array(linedata_without_statement).shape)
    # for i in range(0,1000):
    for i in range(0, number):
        # if TEST_MID == True:
        #     for j in range(0,17):
        #         if(linedata_without_statement[i][j] == '1'):
        #             linedata_without_statement[i][j] = 1
        #         elif(linedata_without_statement[i][j] == '0'):
        #             linedata_without_statement[i][j] = 0
        #         else:
        #             raise Exception("Own_Exception-Function Failed:PcocessStr2IntForLineDataWithoutStatement ERROR")
        if TEST_MID == True:
            for j in range(0,17):
                if(linedata_without_statement[i][j] >= '1'):
                    linedata_without_statement[i][j] = 1
                elif(linedata_without_statement[i][j] == '0'):
                    linedata_without_statement[i][j] = 0
                else:
                    raise Exception("Own_Exception-Function Failed:PcocessStr2IntForLineDataWithoutStatement ERROR")
        elif TEST_BUBBLE == True:
            for j in range(0,21):
                if(linedata_without_statement[i][j] >= '1'):
                    linedata_without_statement[i][j] = 1
                elif(linedata_without_statement[i][j] == '0'):
                    linedata_without_statement[i][j] = 0
                else:
                    raise Exception("Own_Exception-Function Failed:PcocessStr2IntForLineDataWithoutStatement ERROR")
        else:pass
    return linedata_without_statement

pass_fail_result_list = []
def CountTotalPassedFailed(path):
    #open .txt to count the number of TestCase
    actual_recond = open("actual_recond.txt", "r")
    recond = open("../" + path + "recond.txt", "r")
    Lines1 = len(actual_recond.readlines())
    Lines2 = len(recond.readlines())
    actual_recond.close()
    recond.close()
    # print(Lines1,Lines2)#1001 - becasue add the timestap

    actual_recond_lines = []
    actual_recond = open("actual_recond.txt", "r")
    if (Lines1 == Lines2):  # aim for matching the two Testcase number
        for i,val in enumerate(actual_recond):
            # line_actual_recond = val
            actual_recond_lines.append(val)
            # print('line-',i,actual_recond_lines)
    else:
        actual_recond.close()
        recond.close()
        raise Exception("Own_Exception-Function Failed:ount_passed_failed function failed")
    actual_recond.close()

    recond_lines = []
    recond = open("../" + path + "recond.txt", "r")
    if (Lines1 == Lines2):  # aim for matching the two Testcase number
        for i,val in enumerate(recond):
            # line_recond = val
            recond_lines.append(val)
            # print('line',i,recond_lines)
    else:
        actual_recond.close()
        recond.close()
        raise Exception("Own_Exception-Function Failed:ount_passed_failed function failed")
    recond.close()

    print("actual_recond_lines=",np.array(actual_recond_lines).shape)
    print("recond_lines=",np.array(recond_lines).shape)
    # print('Acutal:',actual_recond_lines,'recond:',recond_lines)

    #compare result ,count passed and failed
    total_passed_counter, total_failed_counter= 0, 0

    for i,val in enumerate(recond_lines):
        # print('i:',type(recond_lines[i]),recond_lines[i] , actual_recond_lines[i])
        if(recond_lines[i] == actual_recond_lines[i]):
            pass_fail_result_list.append(0)
            # print(i,'passed')
            total_passed_counter +=1
        else:
            pass_fail_result_list.append(1)
            # print(i,'failed',recond_lines[i],actual_recond_lines[i])
            total_failed_counter +=1

    pass_fail_result_list.remove(pass_fail_result_list[0]) # becasus of the first line is data
    total_failed_counter -=1  #becasus of the first line is data
    print("passed={:d}\tfailed={:d}".format(total_passed_counter,total_failed_counter))

    return total_passed_counter,total_failed_counter

line_count_for_passed =[]

def Get_a_notation(): #获取a_ep, a_np, a_ef, a_nf (passed(p), failed(f), executed(e), not executed(n))
    # file = open("Get_a_notation.txt", "w+")
    # print("\n", "=" * 20, "Get_a_notation", "=" * 20)
    a_np, a_nf, a_ep, a_ef = [], [], [], []

    statement_number = len(linedata[:][0])  # 这里减去5是人工比对 发现有5行是没有coverage
    print("statement_number=", statement_number)
    print("statement_number=", statement_number, file=file)
    for i in range(0, statement_number):
        count, a_np_tmp, a_nf_tmp, a_ep_tmp, a_ef_tmp = 0, 0, 0, 0, 0

        SourceCodeLineIndex.append(linedata[1][i][0])

        #总共1000个TestCase
        for j in range(0, total_file_number):
            # if(linedata[j][i][1] == '1'):
            if (linedata[j][i][1] >= '1'):
            # if(linedata_without_statement[j][i] == '1'):
                count +=1
                if(pass_fail_result_list[j] == 0):#这边注意 因为BPNN passed是0 failed是1,为了统一
                    a_ep_tmp += 1 # passed_count +=1
                else:
                    a_ef_tmp += 1# failed_count +=1
            else:
                count += 1
                if (pass_fail_result_list[j] == 0):  # 这边注意 因为BPNN passed是0 failed是1,为了统一
                    a_np_tmp += 1  # passed_count +=1
                else:
                    a_nf_tmp += 1  # failed_count +=1
        # print("a_np_tmp:{:2d} a_nf_tmp:{:2d}, a_ep_tmp:{:2d}, a_ef_tmp:{:2d}".format(a_np_tmp, a_nf_tmp, a_ep_tmp, a_ef_tmp))
        if(a_np_tmp + a_nf_tmp + a_ep_tmp + a_ef_tmp) != count:
            raise Exception("Own_Exception-Function Failed: (a_np_tmp + a_nf_tmp + a_ep_tmp + a_ef_tmp) != count")
        a_np.append(a_np_tmp)
        a_nf.append(a_nf_tmp)
        a_ep.append(a_ep_tmp)
        a_ef.append(a_ef_tmp)

    # print(np.array(a_np).shape, a_np)
    # print(np.array(a_nf).shape, a_nf)
    # print(np.array(a_ep).shape, a_ep)
    # print(np.array(a_ef).shape, a_ef)

    # file.close()
    return  a_np, a_nf, a_ep, a_ef


def Jaccard():
    start_time = time.time()
    global Jaccard_Time
    file = open("Jaccard.txt", "w+")
    print("\n", "=" * 20, "Jaccard", "=" * 20)
    a_np, a_nf, a_ep, a_ef = Get_a_notation()
    jaccard = []
    statement_number = len(linedata[:][0])  # 这里减去5是人工比对 发现有5行是没有coverage
    print("statement_number=", statement_number)
    print("statement_number=", statement_number, file=file)
    for i in range(0, statement_number):
        jaccard_tmp = a_ef[i] / (a_ef[i] + a_nf[i] + a_ep[i])
        jaccard.append(jaccard_tmp)

    print(np.array(jaccard).shape, jaccard)

    inde_jaccard = []
    print("Jaccard\tThe bug is :", end="")
    for i,val in enumerate(jaccard):
        if val == max(jaccard):
            inde_jaccard.append(jaccard.index(val))
            print(SourceCodeLineIndex[i], end="\t")
    print(max(jaccard), end="\n")

    file.close()

    end_time = time.time()
    Jaccard_Time = end_time - start_time
    print(Jaccard_Time, end_time, start_time)
    return jaccard


def Ochiai2():
    import cmath
    start_time = time.time()
    global Ochiai2_Time
    file = open("ochiai2.txt", "w+")
    print("\n", "=" * 20, "ochiai2", "=" * 20)
    a_np, a_nf, a_ep, a_ef = Get_a_notation()
    ochiai2 = []
    statement_number = len(linedata[:][0])  # 这里减去5是人工比对 发现有5行是没有coverage
    print("statement_number=", statement_number)
    print("statement_number=", statement_number, file=file)
    for i in range(0, statement_number):
        ochiai2_tmp = a_ef[i] * a_nf[i] / \
                      cmath.sqrt( (a_ef[i] + a_ep[i])*(a_np[i] + a_nf[i])*(a_ef[i] + a_nf[i])*(a_ep[i] + a_np[i])  )
        ochiai2.append(ochiai2_tmp)

    print(np.array(ochiai2).shape, ochiai2)
    file.close()

    end_time = time.time()
    Ochiai2_Time = end_time - start_time
    print(Ochiai2_Time, end_time, start_time)
    return ochiai2


def Tarantula():
    start_time = time.time()
    global Tarantula_Time
    file = open("Tarantula.txt","w+")
    print("\n", "=" * 20, "Tarantula", "=" * 20)
    # suspiciousness = [] #Tarantula suspiciousness计算值
    # SourceCodeLineIndex = [] #对应有效代码行信息

    suspiciousness, SourceCodeLineIndex=[], [] #Tarantula suspiciousness计算值 #对应有效代码行信息

    print("linedata",type(linedata), linedata.shape)
    print("linedata", type(linedata), linedata.shape,file=file)
    #计算suspiciousness  15行有效code,每一行为一个statement
    # statement_number = len(linedata[0][:])  #这里减去5是人工比对 发现有5行是没有coverage
    # print("statement_number=",statement_number)
    statement_number = len(linedata[:][0])  #这里减去5是人工比对 发现有5行是没有coverage
    print("statement_number=",statement_number)
    print("statement_number=", statement_number,file=file)
    # for i in range(0,16):#linedata[0][i][1] = 15row  linedata[0][i][0] = 19row
    for i in range(0, statement_number):
        count, passed_count, failed_count = 0, 0, 0

        SourceCodeLineIndex.append(linedata[1][i][0])

        #总共1000个TestCase
        for j in range(0, total_file_number):
            # if(linedata[j][i][1] == '1'):
            if (linedata[j][i][1] >= '1'):
            # if(linedata_without_statement[j][i] == '1'):
                count +=1
                if(pass_fail_result_list[j] == 0):#这边注意 因为BPNN passed是0 failed是1
                    passed_count +=1
                else:
                    failed_count +=1

        if((passed_count + failed_count) == count):
            # print("{:d} {:d} {:d} {:d}".format(passed_count,failed_count,total_passed_counter,total_failed_counter))

            # print(passed_count/total_passed_counter,  passed_count/total_passed_counter,  failed_count/total_failed_counter,\
            #         passed_count/total_passed_counter + failed_count/total_failed_counter)
            tmp = 1 - (passed_count/total_passed_counter)/(passed_count/total_passed_counter + failed_count/total_failed_counter)
            suspiciousness.append(tmp)
            # print(tmp)
        else:
            raise Exception("Own_Exception-Function Failed:(passed_count + failed_count) != count")
                # print(count,linedata[j][i][1])

        # print("i={:2d}\tcount{:d}".format(i,count))

    #拼接成dict
    ScoreDict = {}.fromkeys(SourceCodeLineIndex)

    for i in range(0, statement_number):
        ScoreDict[SourceCodeLineIndex[i]] = [suspiciousness[i]]

    # print("Tarantula suspiciousness ",ScoreDict)
    # print(SourceCodeLineIndex)
    # print(type(suspiciousness))
    # suspiciousness = np.array(suspiciousness)
    # print(type(suspiciousness))
    # print(suspiciousness,'\n',np.array(suspiciousness).shape,'\n')

    max_Tarantula, max_Tarantula_code = [], []

    max_tmp = max(suspiciousness)
    # max_index = suspiciousness.index(max_tmp)
    # max_code = SourceCodeLineIndex[max_index]
    # print('Tarantula max suspiciousness is ', max_tmp, max_code, ScoreDict[max_code])
    # print('Tarantula max suspiciousness is ', max_tmp, max_code, ScoreDict[max_code],file=file)

    print("Tarantula\tThe bug is :", end="")
    for i,val in enumerate(suspiciousness):
        if val == max_tmp:
            max_Tarantula.append(suspiciousness[i])
            max_Tarantula_code.append(SourceCodeLineIndex[i])
            print(SourceCodeLineIndex[i], end="\t")
    print(max(suspiciousness), end="\n")


    # list值排序 并给出对应打下标
    b = sorted(enumerate(suspiciousness),key=lambda x:x[1])
    # print("b ",b,type(b),np.array(b).shape)

    rank = []
    rankDict = {}.fromkeys(SourceCodeLineIndex)
    tmp_rank = list(set(suspiciousness))
    tmp_rank.sort(reverse=True)
    rank_count =[]
    count_tmp = 0
    # 计算 rank
    #计算suspiciousness值重复次数
    for j,val_rank in enumerate(tmp_rank):  #b是有下标值的元组(下标,suspiciousness)
        # print(val_rank)
        count_tmp = 0
        for i,val_sup in enumerate(suspiciousness):
            # print(val_sup)
            if(val_sup == val_rank):
                count_tmp +=1
        rank_count.append(count_tmp)
        print("val_rank({:f})={:d}".format(val_rank,count_tmp))
        print("val_rank({:f})={:d}".format(val_rank, count_tmp),file=file)

    #累加一下重复次数，即最大值是len(rank_count)
    # print(suspiciousness,"\n",)
    # print(tmp_rank,rank_count,len(rank_count))
    for j,val in enumerate(rank_count):
        if(j == 0):
            continue
        else:
            rank_count[j] =val + rank_count[j-1]
    # print(rank_count,len(rank_count))

    #计算 rank 且 拼接成dict
    for i,val_sup in enumerate(suspiciousness):
        count_tmp = 0
        for j,val_rank in enumerate(tmp_rank):
            if (val_sup == val_rank):
                rankDict[SourceCodeLineIndex[i]] = [rank_count[j]] #拼接成dict

    # print("rankDict:",rankDict,'\n',)
    print(suspiciousness, '\n')
    print("rankDict:",rankDict, '\n', file=file)
    # print(ScoreDict,'\n')
    file.close()
    #这边可能字典不好取最大值
    end_time = time.time()
    Tarantula_Time = end_time - start_time
    print(Tarantula_Time, end_time, start_time)
    return ScoreDict,rankDict,SourceCodeLineIndex


def CrossTab():
    start_time = time.time()
    global CrossTab_Time
    file = open("CrossTab.txt","w+")
    print("\n","="*20,"CrossTab","="*20)
    print("=" * 20, "CrossTab", "=" * 20,file=file)
    Chi_Square_list, mu_list, phi_list, xi_list, suspiciousness, SourceCodeLineIndex = [], [], [], [], [], []
    # suspiciousness : Tarantula suspiciousness计算值   SourceCodeLineIndex: 对应有效代码行信息
    print('lindata=',type(linedata), linedata.shape)
    print('lindata=', type(linedata), linedata.shape,file=file)

    #total number of test cases
    N = total_passed_counter + total_failed_counter
    #total number of successful test cases
    Ns = total_passed_counter
    #total number of failed test cases
    Nf = total_failed_counter

    #计算suspiciousness  15行有效code,每一行为一个statement
    # for i in range(0,15):#linedata[0][i][1] = 15row  linedata[0][i][0] = 19row
    statement_number = len(linedata[:][0])
    print("cross Tab", statement_number)
    print("cross Tab", statement_number,file=file)
    for i in range(0, statement_number):
        SourceCodeLineIndex.append(linedata[1][i][0])
        # print(linedata[1][i][0])
        count, Ncw, Ncfw, Ncsw, Nuw, Nufw, Nusw = 0, 0, 0, 0, 0, 0, 0
        # Ncw = 0     #number of test cases covering ω
        # Ncfw = 0    #number of failed test cases covering ω
        # Ncsw = 0    #number of successful test cases covering ω
        # Nuw = 0     #number of test cases not covering ω
        # Nufw = 0    #number of failed test cases not covering ω
        # Nusw = 0    #number of successful test cases not covering ω
        # print('cross tab', total_file_number)
        for j in range(0, total_file_number):
            # if(linedata[j][i][1] == '1'):
            if (linedata[j][i][1] >= '1'):
            # if(linedata_without_statement[j][i] == '1'):
                count +=1
                if(pass_fail_result_list[j] == 0): #这边注意 因为BPNN passed是0 failed是1
                    Ncsw +=1
                else:
                    Ncfw +=1

        # print("Ns={:d}\tNf={:d}".format(Ns, Nf))
        Ncw = Ncsw + Ncfw
        Nuw = N - Ncw
        if(Nuw == 0):
            Nufw, Nusw= 0, 0
        else:
            Nufw, Nusw = abs(Nf - Ncfw), abs(Ns - Ncsw)

        if((Nufw + Nusw) != Nuw):
            raise Exception("Own_Exception-Function Failed: (Nufw + Nusw) != Nuw")

        Ecfw, Ecsw, Eufw, Eusw = (Ncw * Nf) / N, (Ncw * Ns)/N, (Nuw * Nf)/N, (Nuw * Ns)/N

        # print("iter={:d}\tN={:d}\tNs={:d}\tNf={:d}\tNcw={:d}\tNcfw={:d}\tNcsw={:d}\tNuw={:d}\tNufw={:d}\tNusw={:d}". \
        #       format(i, N, Ns, Nf, Ncw, Ncfw, Ncsw, Nuw, Nufw, Nusw))
        #
        # print("iter={:d}\tN={:d}\tNs={:d}\tNf={:d}\tNcw={:d}\t \
        #                        Ncfw={:d}\tNcsw={:d}\tNuw={:d}\tNufw={:d}\tNusw={:d}". \
        #       format(i, N, Ns, Nf, Ncw, Ncfw, Ncsw, Nuw, Nufw, Nusw),file=file)
        # print("Ecfw={:f}\tEcsw={:f}\tEufw={:f}\tEusw={:f}\t".format(Ecfw,Ecsw,Eufw,Eusw))

        if(Nuw == 0):#所有testcase run到了这句代码 比如第一句 所以没有Nuc
            Chi_Square = ((Ncfw - Ecfw) ** 2) / Ecfw + \
                         ((Ncsw - Ecsw) ** 2) / Ecsw
        else:
           Chi_Square = ((Ncfw - Ecfw) ** 2) / Ecfw + \
                     ((Ncsw - Ecsw) ** 2) / Ecsw + \
                     ((Nufw - Eufw) ** 2 )/ Eufw + \
                     ((Nusw - Eusw) ** 2) / Eusw

        '''
        statements with phi>1 and Chi_Square>o have a high degree
        '''

        Chi_Square_list.append(Chi_Square)
        pf = Ncfw / Nf
        if Ncsw == 0 and Ns != 0:
            ps = Ncsw / Ns # ps = 0
            # phi = 9999
            phi = 9999
        else:
            ps = Ncsw / Ns
            phi = pf / ps

        phi_list.append(phi)
        row = 2.0
        col = 2.0
        # mu = (Chi_Square / N)/(math.sqrt((row - 1)(col - 1)))
        mu = (Chi_Square / N)
        mu_list.append(mu)
        if (phi > 1):
            xi =mu
        elif(phi == 1):
            xi = 0
        else:
            xi = 0 - mu
        xi_list.append(xi)

        # print(SourceCodeLineIndex,'\t',
        #         Chi_Square,'\t',
        #         mu,'\t',
        #         phi,xi)

    # print(SourceCodeLineIndex,'\n',
    #         Chi_Square_list,'\n',
    #         mu_list,'\n',
    #         phi_list,'\n',
    #         xi_list)
    index_Chi_Square, index_mu, inde_phi, index_xi = [], [], [], []
    # index_Chi_Square = Chi_Square_list.index(max(Chi_Square_list))
    # index_mu = mu_list.index(max(mu_list))
    # inde_phi = phi_list.index(max(phi_list))
    # index_xi = xi_list.index(max(xi_list))
    print("Based Chi_Square\tThe bug is :", end="")
    for i, val in enumerate(Chi_Square_list):
        if val == max(Chi_Square_list):
            index_Chi_Square.append(Chi_Square_list.index(val))
            print(SourceCodeLineIndex[i], end="\t")
    print(max(Chi_Square_list), "\nBased mu\t\t\tThe bug is :", end="")
    for i, val in enumerate(mu_list):
        if val == max(mu_list):
            index_mu.append(mu_list.index(val))
            print(SourceCodeLineIndex[i], end="\t")
    print(max(mu_list), "\nBased phi\t\t\tThe bug is :", end="")
    for i, val in enumerate(phi_list):
        if val == max(phi_list):
            inde_phi.append(phi_list.index(val))
            print(SourceCodeLineIndex[i], end="\t")
    print(max(phi_list), "\nBased xi\t\t\tThe bug is :", end="")
    for i, val in enumerate(xi_list):
        if val == max(xi_list):
            index_xi.append(xi_list.index(val))
            print(SourceCodeLineIndex[i], end="\t")
    print(max(xi_list), end="\n")

    # print("Based Chi_Square\tThe bug is :{:s}\t max_Chi_square={:f}\tlen={:2d}".format( SourceCodeLineIndex[index_Chi_Square],
    #                                                                                     max(Chi_Square_list),
    #                                                                                     len(Chi_Square_list)))
    # print("Based mu\t\t\tThe bug is :{:s}\t max_mu={:f}\tlen={:2d}".format(SourceCodeLineIndex[index_mu],
    #                                                                                max(mu_list),
    #                                                                                len(mu_list)))
    # print("Based phi\t\t\tThe bug is :{:s}\t max_phi={:f}\tlen={:2d}".format(SourceCodeLineIndex[inde_phi],
    #                                                                                 max(phi_list),
    #                                                                                 len(phi_list)))
    # print("Based xi\t\t\tThe bug is :{:s}\t max_xi={:f}\tlen={:2d}".format( SourceCodeLineIndex[index_xi],
    #                                                                                 max(xi_list),
    #                                                                                 len(xi_list)))

    # print(SourceCodeLineIndex,'\n',
    #       Chi_Square_list,'\n',
    #       mu_list,'\n',
    #       phi_list,'\n',
    #       xi_list)
    file.close()


    # print("Based Chi_Square\tThe bug is :{:s}\t max_Chi_square={:f}\tlen={:2d}".format( SourceCodeLineIndex[index_Chi_Square],
    #                                                                                     max(Chi_Square_list),
    #                                                                                     len(Chi_Square_list)))
    # print("Based mu\t\t\tThe bug is :{:s}\t max_mu={:f}\tlen={:2d}".format(SourceCodeLineIndex[index_mu],
    #                                                                                max(mu_list),
    #                                                                                len(mu_list)))
    # print("Based phi\t\t\tThe bug is :{:s}\t max_phi={:f}\tlen={:2d}".format(SourceCodeLineIndex[inde_phi],
    #                                                                                 max(phi_list),
    #                                                                                 len(phi_list)))
    # print("Based xi\t\t\tThe bug is :{:s}\t max_xi={:f}\tlen={:2d}".format( SourceCodeLineIndex[index_xi],
    #                                                                                 max(xi_list),
    #                                                                                 len(xi_list)))


    end_time = time.time()
    CrossTab_Time = end_time - start_time
    print(CrossTab_Time, end_time, start_time)
    return Chi_Square_list, mu_list, phi_list, xi_list


def BPNeturalNetwork():
    start_time = time.time()
    global BPNeturalNetwork_Time
    file = open("BPNeturalNetwork.txt","w+")
    print("\n","=" * 20, "BPNeturalNetwork", "=" * 20)
    from sklearn.neural_network import MLPClassifier, MLPRegressor
    # print(linedata_without_statement, '\n', np.array(linedata_without_statement).shape)
    # print(pass_fail_result_list, '\n', np.array(pass_fail_result_list).shape)

    # BPclf = MLPClassifier(#solver = 'sgd',
    #                       hidden_layer_sizes= 3,
    #                       activation= 'logistic',
    #                      learning_rate= 'adaptive',
    #                      )
    # for Bubble
    BPclf = MLPRegressor(#solver = 'sgd',
                          max_iter=200,
                          hidden_layer_sizes= 30,
                          activation= 'logistic',
                          learning_rate= 'adaptive',
                          alpha=0.0001,
                          learning_rate_init=0.001,
                         )
    # for mid
    # BPclf = MLPRegressor(#solver = 'sgd',
    #                       max_iter=1000,
    #                       hidden_layer_sizes= 10,
    #                       activation= 'logistic',
    #                       learning_rate= 'adaptive',
    #                       alpha=0.0001,
    #                       learning_rate_init=0.001,
    #                       momentum=0.9,
    #                      )
    # print(BPclf)
    # print(BPclf,file=file)

    BPclf.fit(linedata_without_statement,pass_fail_result_list)
    weights = np.array(BPclf.coefs_)
    bias = np.array(BPclf.intercepts_)
    # print("weight:",BPclf.coefs_,"\nbias:",BPclf.intercepts_)
    # print("weight:",weights,"\nbias:",bias)
    # print("weight:",weights.shape, "\nbias:",bias.shape)

    # print(BPclf.loss_)
    # print(BPclf.classes_)
    if TEST_MID == True:
        Cvx = np.eye(17)
    elif TEST_BUBBLE == True:
        Cvx = np.eye(21)
    else:pass
    # print(Cvx,Cvx.shape)

    pred = BPclf.predict(Cvx)
    print(type(pred))
    # print(pred,"max=",max(pred),"\n",
    #       "max=",SourceCodeLineIndex[np.argmax(pred, axis=0)],'\t',np.argmax(pred, axis=0),pred[np.argmax(pred, axis=0)],'\n',
    #       "min=",SourceCodeLineIndex[np.argmin(pred, axis=0)],'\t',np.argmin(pred, axis=0),pred[np.argmin(pred, axis=0)],'\n',
    #       "The bug: ",SourceCodeLineIndex[np.argmax(pred, axis=0)],np.argmax(pred, axis=0),pred[np.argmax(pred, axis=0)],)
    #
    # print(pred,"max=",max(pred),"\n",
    #       "max=",SourceCodeLineIndex[np.argmax(pred, axis=0)],'\t',np.argmax(pred, axis=0),pred[np.argmax(pred, axis=0)],'\n',
    #       "min=",SourceCodeLineIndex[np.argmin(pred, axis=0)],'\t',np.argmin(pred, axis=0),pred[np.argmin(pred, axis=0)],'\n',
    #       "The bug: ",SourceCodeLineIndex[np.argmax(pred, axis=0)],np.argmax(pred, axis=0),pred[np.argmax(pred, axis=0)],
    #       file=file)

    print(pred,"max=",max(pred),"\n",
          "max=",SourceCodeLineIndex[np.argmax(pred, axis=0)],'\t\t',pred[np.argmax(pred, axis=0)],'\n',
          "min=",SourceCodeLineIndex[np.argmin(pred, axis=0)],'\t\t',pred[np.argmin(pred, axis=0)],'\n',
          "The bug: ",SourceCodeLineIndex[np.argmax(pred, axis=0)],pred[np.argmax(pred, axis=0)],)

    # print(pred,"max=",max(pred),"\n",
    #       "max=",SourceCodeLineIndex[np.argmax(pred, axis=0)],'\t\t',pred[np.argmax(pred, axis=0)],'\n',
    #       "min=",SourceCodeLineIndex[np.argmin(pred, axis=0)],'\t\t',pred[np.argmin(pred, axis=0)],'\n',
    #       "The bug: ",SourceCodeLineIndex[np.argmax(pred, axis=0)],pred[np.argmax(pred, axis=0)],
    #       file=file)

    # print(BPclf.loss_, "\n", BPclf.coefs_, "\n", BPclf.intercepts_, "\n",BPclf.n_iter_, "\n",BPclf.n_layers_,"\n", BPclf.n_outputs_, "\n",BPclf.out_activation_)
    print("Loss:",BPclf.loss_)
    print(BPclf.out_activation_)
    # # print(SourceCodeLineIndex[10])

    # pred_sort = sorted(pred)
    # print(pred_sort,"max_after_sort ",max(pred))

    pred_sort = sorted(enumerate(pred),key=lambda x:x[1])
    # print("pred_sort ",pred_sort,type(pred_sort),np.array(pred_sort).shape)
    # print(max(pred_sort),pred_sort[1][1])

    BP_rank =[]
    # print(sorted(pred_sort_again))
    if TEST_MID == True:
        for i in range(0,17):
            BP_rank.append(SourceCodeLineIndex[pred_sort[16-i][0]])
            # print("x", SourceCodeLineIndex[pred_sort[16 - i][0]])
            # print("x", SourceCodeLineIndex[pred_sort[16 - i][0]],file=file)
    elif TEST_BUBBLE == True:
        for i in range(0,21):
            BP_rank.append(SourceCodeLineIndex[pred_sort[20-i][0]])
    else:pass

    print(BP_rank)
    file.close()

    end_time = time.time()
    BPNeturalNetwork_Time = end_time - start_time
    print(BPNeturalNetwork_Time, end_time, start_time)
    return BP_rank

    
def BPNN_method():
    start_time = time.time()
    global BPNN_method_Time
    file = open("BPNN_method.txt","w+")
    print("\n","=" * 20, "BPNN_method", "=" * 20)
    from sklearn.neural_network import MLPClassifier, MLPRegressor
    # print(linedata_without_statement)
    # print(pass_fail_result_list)
    failed_index = []

    fail_testcase_statement = []

    for i,val in enumerate(linedata_without_statement):
        if pass_fail_result_list[i] == 1:
            fail_testcase_statement.append(val)

    # print(fail_testcase_statement)              
    transpose_fail_testcase_statement = np.transpose(fail_testcase_statement)
    print('transpose_fail_testcase_statement',transpose_fail_testcase_statement)
    print('shape:',np.array(transpose_fail_testcase_statement).shape)

    print('transpose_fail_testcase_statement',transpose_fail_testcase_statement,file=file)
    print('shape:',np.array(transpose_fail_testcase_statement).shape,file=file)

    BPNN_rank = []
    for i,val in enumerate(transpose_fail_testcase_statement):
        # print(i)
        for j,val_statement in enumerate(val):
            if(val_statement == 0) :
                flag_j = 0
                continue
            else :
               flag_j = 1
        BPNN_rank.append(flag_j)       
    print(BPNN_rank, np.array(BPNN_rank).shape)
    print(BPNN_rank, np.array(BPNN_rank).shape,file=file)
    # print(np.array(fail_testcase_statement).shape)  
    # print(fail_testcase_statement)        
    # BPclf = MLPClassifier(#solver = 'sgd',
    #                       hidden_layer_sizes= 3,
    #                       activation= 'logistic',
    #                      learning_rate= 'adaptive',
    #                      )

    BPclf = MLPRegressor(#solver = 'sgd',
                          max_iter=800,
                          hidden_layer_sizes= 3,
                          activation= 'logistic',
    #                      learning_rate= 'adaptive',
                         )
    print(BPclf)
    print(BPclf,file=file)
    BPclf.fit(linedata_without_statement, pass_fail_result_list)
    weights = np.array(BPclf.coefs_)
    bias = np.array(BPclf.intercepts_)
    # print("weight:",BPclf.coefs_,"\nbias:",BPclf.intercepts_)
    # print("weight:",weights,"\nbias:",bias)
    # print("weight:",weights.shape, "\nbias:",bias.shape)

    # print(BPclf.loss_)
    # print(BPclf.classes_)
    if TEST_MID == True:
        Cvx = np.eye(17)
    elif TEST_BUBBLE == True:
        Cvx = np.eye(21)
    else:pass
    # print(Cvx,Cvx.shape)

    pred = BPclf.predict(Cvx)
    # print(type(pred))
    print(pred,"max=",max(pred),"\n",
          "max=",SourceCodeLineIndex[np.argmax(pred, axis=0)],'\t',np.argmax(pred, axis=0),pred[np.argmax(pred, axis=0)],'\n',
          "min=",SourceCodeLineIndex[np.argmin(pred, axis=0)],'\t',np.argmin(pred, axis=0),pred[np.argmin(pred, axis=0)],'\n',
          "The bug: ",SourceCodeLineIndex[np.argmax(pred, axis=0)],np.argmax(pred, axis=0),pred[np.argmax(pred, axis=0)],)

    print(pred,"max=",max(pred),"\n",
          "max=",SourceCodeLineIndex[np.argmax(pred, axis=0)],'\t',np.argmax(pred, axis=0),pred[np.argmax(pred, axis=0)],'\n',
          "min=",SourceCodeLineIndex[np.argmin(pred, axis=0)],'\t',np.argmin(pred, axis=0),pred[np.argmin(pred, axis=0)],'\n',
          "The bug: ",SourceCodeLineIndex[np.argmax(pred, axis=0)],np.argmax(pred, axis=0),pred[np.argmax(pred, axis=0)],
          file=file)

    # print(SourceCodeLineIndex[10])

    # pred_sort = sorted(pred)
    # print(pred_sort,"max_after_sort ",max(pred))

    pred_sort = sorted(enumerate(pred),key=lambda x:x[1])
    # print("pred_sort ",pred_sort,type(pred_sort),np.array(pred_sort).shape)
    # print(max(pred_sort),pred_sort[1][1])

    BP_rank =[]
    # print(sorted(pred_sort_again))
    if TEST_MID == True:
        for i in range(0,17):
            BP_rank.append(SourceCodeLineIndex[pred_sort[16-i][0]])
            # print("x", SourceCodeLineIndex[pred_sort[16 - i][0]])
            # print("x", SourceCodeLineIndex[pred_sort[16 - i][0]],file=file)
    elif TEST_BUBBLE == True:
        for i in range(0,21):
            BP_rank.append(SourceCodeLineIndex[pred_sort[20-i][0]])
    else:pass

    print('shape:',np.array(BP_rank).shape)
    print('BP_rank:',BP_rank,)

    print('shape:',np.array(BP_rank).shape,file=file)
    print('BP_rank:',BP_rank,file=file)

    file.close()

    end_time = time.time()
    BPNN_method_Time = end_time - start_time
    print(BPNN_method_Time, end_time, start_time)
    return BP_rank


if __name__ == '__main__':
    file = open("main.txt","w+")
    filecount = GetTestCaseNumber()

    TestCaseFilename, total_file_number = ProcessTestCaseFilename(filecount)

    for TestCaseFilename in TestCaseFilename:
        ProcessOneCsv(TestCaseFilename)
        # print(linedata)

    # PcocessStr2IntForLineDataWithoutStatement()
    PcocessStr2IntForLineDataWithoutStatement(total_file_number)
    # print(linedata_without_statement)

    if TEST_BUBBLE == True:
        ActualBubble(5, 5, 10, 5)
    elif TEST_MID == True:
        ActualMid(10,10,10)
    else:pass

    total_passed_counter,total_failed_counter = CountTotalPassedFailed(testcase_PATH)
    # print("total_passed_counter={:d}\ttotal_failed_counter={:d}".format(total_passed_counter,total_failed_counter))

    linedata = np.array(linedata)
    linedata_without_statement = np.array(linedata_without_statement)

    Tarantula_ScoreDict,Tarantula_rankDict,SourceCodeLineIndex =Tarantula()

    # print(SourceCodeLineIndex)

    jaccard = Jaccard()

    Chi_Square_list, mu_list , phi_list , xi_list = CrossTab()
    # print(type(linedata),linedata.shape)
    # print(linedata,'\n',np.array(linedata).shape)

    BP_rank = BPNeturalNetwork()

    print("RunningTime:\nJaccard_Time:\t\t\t\t{:.10f}\nTarantula_Time:\t\t\t\t{:.10f}\nCrossTab_Time:\t\t\t\t{:.10f}\nBPNeturalNetwork_Time:\t\t{:.10f}\n".format(
        Jaccard_Time, Tarantula_Time, CrossTab_Time, BPNeturalNetwork_Time))

    print("RunningTime:\nJaccard_Time:\t\t\t\t{:.10f}\nTarantula_Time:\t\t\t\t{:.10f}\nCrossTab_Time:\t\t\t\t{:.10f}\nBPNeturalNetwork_Time:\t\t\t{:.10f}\n".format(
        Jaccard_Time, Tarantula_Time, CrossTab_Time, BPNeturalNetwork_Time),file=file)

    print(testcase_PATH)

    Testprogram = open("../" + testcase_PATH + "test.c","r")
    for i,line in enumerate(Testprogram):
        print(i+1,"\t", line,end="")
        print(i+1,"\t", line,end="",file=file)

    # print(linedata,)
    # print("linedata= ",linedata.shape)

    column = []
    for i in range(np.array(linedata_without_statement).shape[1]):
        column.append(linedata[0][i][0])
    # print(column, "\n",np.array(column).shape)

    pd_linedata_without_statement = DataFrame(linedata_without_statement,columns=column)
    print(pd_linedata_without_statement, file=file)
    print("linedata_without_statement= ",pd_linedata_without_statement.shape, file=file)

    file.close()

