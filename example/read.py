# -*-coding:utf-8-*-
import csv
def traj_read(filename):
    dataDict = dict()           #构建一个字典存放数据

    # csvfile = open(filename, 'r', encoding='utf8')
    csvfile = open(filename, 'r')
    reader = csv.DictReader(csvfile)
    # print(reader)  # <csv.DictReader object at 0x000002241D730FD0>
    key = ["t", "p_x", "p_y", "p_z", "q_w", "q_x", "q_y", "q_z", "v_x", "v_y", "v_z", "w_x", "w_y", "w_z", "u_1", "u_2", "u_3", "u_4"]
    for i in key:
        dataDict[i] = []

    for row in reader:
        for index,i in enumerate(key):
            # print(index)
            dataDict[i].append(float(row[i]))

    return [dataDict[i] for i in key]
    # return dataDict["t"],dataDict["p_x"],dataDict["p_y"],dataDict["p_z"],dataDict["q_w"],dataDict["q_x"],dataDict["q_y"],dataDict["q_z"],dataDict["v_x"],dataDict["v_y"],dataDict["v_z"],dataDict["w_x"],dataDict["w_y"],dataDict["w_z"],dataDict["u_1"],dataDict["u_2"],dataDict["u_3"],dataDict["u_4"]

def traj_BinarySearch(time, t_list):
    start_index = 0
    end_index = len(t_list)-1
    
    while(start_index < end_index):
        middle = int((start_index + end_index))/2
        # print(t_list[middle])
        if t_list[middle] <= time:
            start_index = middle +1
        else:
            end_index = middle -1
    
    if abs(t_list[start_index] - time) <= abs(t_list[end_index] - time):
        print(t_list[start_index],t_list[end_index])
        return start_index,t_list[start_index]
    else:
        print(t_list[start_index],t_list[end_index])
        return end_index,t_list[end_index]
        
def traj_search(time, t_list):
    pointer = 0
    while(pointer < len(t_list)-1):
        if time < t_list[pointer]:
            return pointer,t_list[pointer]
        else:
            pointer += 1

    return pointer,t_list[(len(t_list)-1)]


if __name__ == '__main__':
    [t,p_x,p_y,p_z,q_w,q_x,q_y,q_z,v_x,v_y,v_z,w_x,w_y,w_z,u_1,u_2,u_3,u_4] = traj_read('/home/syy/Racing/time_optimal_trajectory/example/result.csv')
    # t_index,time = traj_BinarySearch(0.5 , t)
    # print(t)
    # time = traj_search(0.1, t)
    # print(time)
    # print(t_index,time)
    # print(type(p_z[0]))

    pointer,time = traj_search(50, t)
    print(pointer,time)
    # a = 0
    # while(a<100):
    #     t_now = traj_search(time, t)
    #     print(t_now)
    #     time = time + 0.05 

    


