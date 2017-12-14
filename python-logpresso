import json     # json 처리
import sys      # system 입출력
import pandas as pd                     # 데이터 프레임 생성
from itertools import chain             # 딕셔너리 병합
from collections import defaultdict     # 딕셔너리 병합







########## JSON -> Dictionary #############################
listDict = []
for line in sys.stdin:  # 로그프레소에 들어오는 입력 데이터 ( sys.stdin )
    listDict.append(json.loads(line))

# print(listDict)     # 로그프레소에서 들어오는 최종 데이터 형태

###################################################################################################################
# dict1 = {'_id':1, 'idle':98, 'kernel':0, 'user':2}     # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# dict2 = {'_id':2, 'idle':76, 'kernel':14, 'user':10}   # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# dict3 = {'_id':3, 'idle':99, 'kernel':1, 'user':0}     # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# dict4 = {'_id':4, 'idle':90, 'kernel':8, 'user':2}     # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# dict5 = {'_id':5, 'idle':88, 'kernel':10, 'user':2}    # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
#                                                        # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# listDict = []                                          # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# listDict.append(dict1)                                 # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# listDict.append(dict2)                                 # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# listDict.append(dict3)                                 # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# listDict.append(dict4)                                 # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# listDict.append(dict5)                                 # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
#                                                        # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
# print(listDict)                                        # 로그프레소로부터 입력받은 데이터와 같은 형태의 샘플 생성
###################################################################################################################










########## Dictionary -> DataFrame #############################
mergedDict = defaultdict(list)      # 딕셔너리 병합 [ 다중 딕셔너리들의 key, value 조인 ]
for line in listDict:
    for key, value in chain(line.items()):
        mergedDict[key].append(value)

df = pd.DataFrame(data=mergedDict)  # 딕셔너리를 데이터 프레임 형태로 변환

# print(df)   # 분석 준비된 최종 데이터 형태 (데이터 프레임)







########## Machine Learning #############################
# 분석 시작
#     -
#     -
#     -
#     -
#     -
#     -
#     -
# 분석 종료







########## DataFrame -> Dictionary #############################
resultDict = df.to_dict(orient='records')   # 데이터 프레임을 딕셔너리 형태로 변환
# print(resultDict)   # 로그프레소에 입력되는 최종 데이터 형태







########## Dictionary -> JSON #############################
for line in resultDict:
    print(json.dumps(line, default=str))     # 로그프레소에 결과 출력
