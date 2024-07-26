import numpy as np
import cv2
import glob

def combine_label_parallel(ls_file, height, width):
    start_index = 0
    for i in range(len(ls_file)-1):
        grasp_angle = np.zeros((height,width))
        grasp_center = np.zeros((height,width))
        split_file_name1 = ls_file[i].split('-')
        split_file_name2 = ls_file[i+1].split('-')
        if int(split_file_name1[1])!=int(split_file_name2[1]):
            for j in range(start_index, i+1):
                if int(ls_file[j].split('-')[7]) != 12:
                    temp1 = cv2.imread(ls_file[j])[:,:,0]
                    grasp_center = grasp_center + temp1
                    grasp_center = np.where(grasp_center!=0,127,grasp_center)
                    temp_angle = cv2.imread(ls_file[j])[:,:,0]
                    temp_angle = np.where(temp_angle==255,1,0)
                    grasp_angle = grasp_angle + (grasp_angle==0)*temp_angle*int(ls_file[j].split('-')[7])
                else:
                    temp2 = cv2.imread(ls_file[j])[:,:,0]
                    temp2 = np.where(temp2==0,255,0)
            start_index = i + 1
            grasp_center = grasp_center + temp2
            print(np.amax(grasp_angle))
            print(np.amin(grasp_angle))
            #grasp_center = grasp_center.astype(np.uint8)
            cv2.imwrite('/home/buitathieu/Downloads/combine_label/'+ls_file[j].split('-')[1]+'.png', grasp_center)
            cv2.imwrite('/home/buitathieu/Downloads/combine_angle/'+ls_file[j].split('-')[1]+'.png', grasp_angle)

if __name__ == "__main__":
    ls_file = sorted(glob.glob('/home/buitathieu/Downloads/realdata_label_example/*.png'))
    combine_label_parallel(ls_file, height=480, width=640)
