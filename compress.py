# -*- coding: utf-8 -*-
 
from numpy import *
import PIL.Image 
screenLevels = 255.0
#4x4 pixel

#yuv_file = "test1280x720.yuv"
#width = 1280 
#height = 720 

#yuv_file = "test352x288.yuv"
#width = 352 
#height = 288 

yuv_file = "test160x160.yuv"
width = 160 
height = 160 


sby_num = width*height//16
sbuv_num = sby_num//4


Ypixel=[ [0]*16 for row in range(0,sby_num )] 
Upixel=[ [0]*16 for row in range(0,sbuv_num)] 
Vpixel=[ [0]*16 for row in range(0,sbuv_num)] 

sbh = (int)(height/4)
sbw = (int)(width/4)
uv_sbh = (int)(height/8)
uv_sbw = (int)(width/8)

HV_copy_sbnum = 0



def yuv_import(filename,dims,numfrm,startfrm):
    fp=open(filename,'rb')
    #print(prod(dims))
    blk_size = (dims[0] * dims[1]*3/2)
    seek_len = (int)(blk_size*startfrm)
    #print(seek_len)
    fp.seek(seek_len,0)
    Y=[]
    U=[]
    V=[]
    #print dims[0]
    #print dims[1]
    d00=dims[0]//2
    d01=dims[1]//2
    #print(d00)
    #print(d01)
    Yt=zeros((dims[0],dims[1]),uint8,'C')
    Ut=zeros((d00,d01),uint8,'C')
    Vt=zeros((d00,d01),uint8,'C')
    for i in range(numfrm):
        for m in range(dims[0]):
            for n in range(dims[1]):
                #print m,n
                Yt[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Ut[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Vt[m,n]=ord(fp.read(1))
        Y=Y+[Yt]
        U=U+[Ut]
        V=V+[Vt]

    width = dims[0]
    height = dims[1]

    global Ypixel
    global Upixel
    global Vpixel

    for idy in range(sbh):
        for idx in range(sbw):
            newx = idx*4+0   
            newy0 = (idy*4+0) 
            newy1 = (idy*4+1) 
            newy2 = (idy*4+2) 
            newy3 = (idy*4+3) 
            #print("newy3:" + str(newy3))
            #print("newx:" + str(newx))
            #ltmp = [] 
              
            #ltmp =  [Yt[newx,newy0], Yt[newx+1,newy0], Yt[newx+2,newy0], Yt[newx+3,newy0], 
            #         Yt[newx,newy1], Yt[newx+1,newy1], Yt[newx+2,newy1], Yt[newx+3,newy1],   
            #         Yt[newx,newy2], Yt[newx+1,newy2], Yt[newx+2,newy2], Yt[newx+3,newy2],  
            #         Yt[newx,newy3], Yt[newx+1,newy3], Yt[newx+2,newy3], Yt[newx+3,newy3]]


            Ypixel[idx+idy*sbw] = [Yt[newx,newy0], Yt[newx+1,newy0], Yt[newx+2,newy0], Yt[newx+3,newy0], 
                     Yt[newx,newy1], Yt[newx+1,newy1], Yt[newx+2,newy1], Yt[newx+3,newy1],   
                     Yt[newx,newy2], Yt[newx+1,newy2], Yt[newx+2,newy2], Yt[newx+3,newy2],  
                     Yt[newx,newy3], Yt[newx+1,newy3], Yt[newx+2,newy3], Yt[newx+3,newy3]]

            #print("sbidx"+str(idx+idy*sbw))
            #print(Ypixel[idx+idy*sbw])


    for idy in range(uv_sbh):
        for idx in range(uv_sbw):
            newx = idx*4+0   
            newy0 = (idy*4+0) 
            newy1 = (idy*4+1) 
            newy2 = (idy*4+2) 
            newy3 = (idy*4+3) 
            Upixel[idx+idy*uv_sbw] =  [Ut[newx,newy0], Ut[newx+1,newy0], Ut[newx+2,newy0], Ut[newx+3,newy0],  
                                       Ut[newx,newy1], Ut[newx+1,newy1], Ut[newx+2,newy1], Ut[newx+3,newy1],  
                                       Ut[newx,newy2], Ut[newx+1,newy2], Ut[newx+2,newy2], Ut[newx+3,newy2],  
                                       Ut[newx,newy3], Ut[newx+1,newy3], Ut[newx+2,newy3], Ut[newx+3,newy3]]

            #print("usbidx"+str(idx+idy*uv_sbw))
            #print(Upixel[idx+idy*uv_sbw])
   	
    for idy in range(uv_sbh):
        for idx in range(uv_sbw):
            newx = idx*4+0   
            newy0 = (idy*4+0) 
            newy1 = (idy*4+1) 
            newy2 = (idy*4+2) 
            newy3 = (idy*4+3) 
            Vpixel[idx+idy*uv_sbw] =  [Vt[newx,newy0], Vt[newx+1,newy0], Vt[newx+2,newy0], Vt[newx+3,newy0],  
                                       Vt[newx,newy1], Vt[newx+1,newy1], Vt[newx+2,newy1], Vt[newx+3,newy1],   
                                       Vt[newx,newy2], Vt[newx+1,newy2], Vt[newx+2,newy2], Vt[newx+3,newy2],  
                                       Vt[newx,newy3], Vt[newx+1,newy3], Vt[newx+2,newy3], Vt[newx+3,newy3]]
   	

            #print("vsbidx"+str(idx+idy*uv_sbw))
            #print(Vpixel[idx+idy*uv_sbw])


		
    fp.close()
    return (Y,U,V)
	
def get_bits(val):
    if(val>=256 and val < 512):
        return 9
    elif(val>=128 and val < 256):
        return 8 
    elif(val>=64 and val < 128):
        return 7 
    elif(val>=32 and val < 64):
        return 6 
    elif(val>=16 and val < 32):
        return 5 
    elif(val>= 8 and val < 16):
        return 4 
    elif(val>= 4 and val < 8):
        return 3 
    elif(val>= 2 and val < 4):
        return 2 
    elif(val>= 0 and val < 2):
        return 1 
    else:
        print("======================Error in get_bits===================")
        print("======================Error in get_bits===================")

def zero_cnt(src):
    cnt = 0
    #print("src")
    #print(src)
    if(src==[0,0,0,0]):
        cnt = 4
    elif(( (int)(src[0]==0) + (int)(src[1]==0) + (int)(src[2]==0) + (int)(src[3]==0))==3):
        cnt = 3 
    elif((src[0:2]==[0,0]) or (src[1:3] == [0,0]) or (src[2:4] == [0,0])):
        cnt = 2
        #print(src)
        #print("has zero2----------------------------------------------------------------------------")
    else:
        cnt = 1
    return cnt



def compress(pred,src,is_h,is_v,is_dc, has_left, has_top):
     # src[0]  src[1]  src[2]  src[3]
     # src[4]  src[5]  src[6]  src[7]
     # src[8]  src[9]  src[10] src[11]
     # src[12] src[13] src[14] src[15]
    if(is_h):
        rs00 = src[0]   #- pred[0]
        rs01 = src[1]   #- pred[0]
        rs02 = src[2]   #- pred[0]
        rs03 = src[3]   #- pred[0]
        
        rs10 = src[4]   #- pred[1]
        rs11 = src[5]   #- pred[1]
        rs12 = src[6]   #- pred[1]
        rs13 = src[7]   #- pred[1]

        rs20 = src[8 ]  # - pred[2]
        rs21 = src[9 ]  # - pred[2]
        rs22 = src[10]  # - pred[2]
        rs23 = src[11]  # - pred[2]

        rs30 = src[12]  # - pred[3]
        rs31 = src[13]  # - pred[3]
        rs32 = src[14]  # - pred[3]
        rs33 = src[15]  # - pred[3]




    elif(is_v):
        rs00 = src[0]   #- pred[0]
        rs01 = src[4]   #- pred[0]
        rs02 = src[8]   #- pred[0]
        rs03 = src[12]  # - pred[0]
        
        rs10 = src[1]   #- pred[1]
        rs11 = src[5]   #- pred[1]
        rs12 = src[9]   #- pred[1]
        rs13 = src[13]  # - pred[1]

        rs20 = src[2 ]  # - pred[2]
        rs21 = src[6 ]  # - pred[2]
        rs22 = src[10]  # - pred[2]
        rs23 = src[14]  # - pred[2]

        rs30 = src[3]   #- pred[3]
        rs31 = src[7]   #- pred[3]
        rs32 = src[11]  # - pred[3]
        rs33 = src[15]  # - pred[3]

    elif(is_dc):
        rs00 = src[0]   #- pred[0]
        rs01 = src[1]   #- pred[0]
        rs02 = src[4]   #- pred[0]
        rs03 = src[5]   #- pred[0]

        rs10 = src[2]   #- pred[1]
        rs11 = src[3]   #- pred[1]
        rs12 = src[6]   #- pred[1]
        rs13 = src[7]   #- pred[1]

        rs20 = src[8]   #- pred[2]
        rs21 = src[9]   #- pred[2]
        rs22 = src[12]  # - pred[2]
        rs23 = src[13]  # - pred[2]

        rs30 = src[10]  # - pred[3]
        rs31 = src[11]  # - pred[3]
        rs32 = src[14]  # - pred[3]
        rs33 = src[15]  # - pred[3]

    else:
        rs00 = src[0]   #- pred[0]
        rs01 = src[1]   #- pred[0]
        rs02 = src[2]  # - pred[0]
        rs03 = src[3]  # - pred[0]

        rs10 = src[4]   #- pred[1]
        rs11 = src[5]   #- pred[1]
        rs12 = src[8]   #- pred[1]
        rs13 = src[9]  # - pred[1]

        rs20 = src[6]   #- pred[2]
        rs21 = src[7]   #- pred[2]
        rs22 = src[10]   #- pred[2]
        rs23 = src[11]   #- pred[2]

        rs30 = src[12]   #- pred[3]
        rs31 = src[13]  # - pred[3]
        rs32 = src[14]  # - pred[3]
        rs33 = src[15]  # - pred[3]

    #if( rs00 ==  pred[0]   and 
    #    rs01 ==  pred[0]   and   
    #    rs02 ==  pred[0]   and  
    #    rs03 ==  pred[0]   and  
    #    rs10 ==  pred[1]   and  
    #    rs11 ==  pred[1]   and  
    #    rs12 ==  pred[1]   and  
    #    rs13 ==  pred[1]   and  
    #    rs20 ==  pred[2]   and  
    #    rs21 ==  pred[2]   and 
    #    rs22 ==  pred[2]   and 
    #    rs23 ==  pred[2]   and 
    #    rs30 ==  pred[3]   and 
    #    rs31 ==  pred[3]   and 
    #    rs32 ==  pred[3]   and 
    #    rs33 ==  pred[3]   and ( (has_left and is_h) or (has_top and is_v) ) ): 
    #    print("v H copy mode")
    #    return 2 



    #print(rs00,rs01,rs02,rs03)
    #print(rs10,rs11,rs12,rs13)
    #print(rs20,rs21,rs22,rs23)
    #print(rs30,rs31,rs32,rs33)
    global HV_copy_sbnum



    #if([rs00,rs01,rs02,rs03,rs10,rs11,rs12,rs13,rs20,rs21,rs22,rs23,rs30,rs31,rs32,rs33] == ([0]*16)):
    #   HV_copy_sbnum+=1
    #   print("copy ")
    #    return 0
    #else:
    min0 = min(rs00,rs01,rs02,rs03)
    min1 = min(rs10,rs11,rs12,rs13)
    min2 = min(rs20,rs21,rs22,rs23)
    min3 = min(rs30,rs31,rs32,rs33)

    min_tr = min(min0,min1,min2,min3)

    min_rs0 = min0 - min_tr
    min_rs1 = min1 - min_tr
    min_rs2 = min2 - min_tr
    min_rs3 = min3 - min_tr
 
    min_rs_max = max(min_rs0,min_rs2,min_rs2,min_rs3)
        
    rs0_sub_max = max(rs00-min0,rs01-min0,rs02-min0,rs03-min0)
    rs1_sub_max = max(rs10-min1,rs11-min1,rs12-min1,rs13-min1)
    rs2_sub_max = max(rs20-min2,rs21-min2,rs22-min2,rs23-min2)
    rs3_sub_max = max(rs30-min3,rs31-min3,rs32-min3,rs33-min3)



    k0 = get_bits(min_rs_max)
    k1 = get_bits(rs0_sub_max)
    k2 = get_bits(rs1_sub_max)
    k3 = get_bits(rs2_sub_max)
    k4 = get_bits(rs3_sub_max)

    #zero_cnt0 = (int)(min_rs0==0) + (int)(min_rs1==0) + (int)(min_rs2==0) + (int)(min_rs3==0)
    #zero_cnt1 = (int)(rs00==min0) + (int)(rs01==min0) + (int)(rs02==min0) + (int)(rs03==min0)
    #zero_cnt2 = (int)(rs10==min1) + (int)(rs11==min1) + (int)(rs12==min1) + (int)(rs13==min1)
    #zero_cnt3 = (int)(rs20==min2) + (int)(rs21==min2) + (int)(rs22==min2) + (int)(rs23==min2)
    #zero_cnt4 = (int)(rs30==min3) + (int)(rs31==min3) + (int)(rs32==min3) + (int)(rs33==min3)

    zero_cnt0 = zero_cnt([min_rs0,min_rs1,min_rs2,min_rs3])
    zero_cnt1 = zero_cnt([rs00-min0,rs01-min0,rs02-min0,rs03-min0])
    zero_cnt2 = zero_cnt([rs10-min1,rs11-min1,rs12-min1,rs13-min1])
    zero_cnt3 = zero_cnt([rs20-min2,rs21-min2,rs22-min2,rs23-min2])
    zero_cnt4 = zero_cnt([rs30-min3,rs31-min3,rs32-min3,rs33-min3])

    #print("zero " + (str)(zero_cnt0)  + " "  + (str)(zero_cnt1) + " " + (str)(zero_cnt2) + " " + (str)(zero_cnt3) + " " + (str)(zero_cnt4))
    
    #bits = 28 + 4*(k0+k1+k2+k3+k4)
    #bits = 28 + (4-zero_cnt0)*k0 + (4-zero_cnt1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
    #bits = 28 + 4*k0 + (4-zero_cnt1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
    if(zero_cnt0==4 and zero_cnt1==4 and zero_cnt2==4 and zero_cnt3==4 and zero_cnt4==4):
        bits = 8+4
        print("all pixel is the same in the 4x4 block")
        print(src)
        print(pred)
    else:
        #bits = 28 + (4-zero_cnt0)*k0 + (4-zero_cnt1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
        #bits = 30 + (4-zero_cnt0)*k0 + (4-zero_cnt1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
        k0_bits = 0 if(zero_cnt0==4) else (3*k0 + 2)
        k1_bits = 0 if(zero_cnt1==4) else (3*k1 + 2)

               

        k2_bits = 0 if((zero_cnt2==4) or ([rs10,rs11,rs12,rs13] == [rs00,rs01,rs02,rs03])) else (3*k2 + 2)
        k3_bits = 0 if((zero_cnt3==4) or ([rs20,rs21,rs22,rs23] == [rs00,rs01,rs02,rs03] or [rs20,rs21,rs22,rs23] == [rs10,rs11,rs12,rs13] )) else (3*k3 + 2)
        k4_bits = 0 if((zero_cnt4==4) or ([rs30,rs31,rs32,rs33] == [rs00,rs01,rs02,rs03] or [rs30,rs31,rs32,rs33] == [rs10,rs11,rs12,rs13]  or [rs30,rs31,rs32,rs33] == [rs20,rs21,rs22,rs23] )) else (3*k4 + 2)

        #bits = 30 + (4-zero_cnt0)*k0 + (4t1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
        bits = 30 + k0_bits + k1_bits + k2_bits + k3_bits + k4_bits 

    if(bits<128):
        return bits
    else:
        return 128

	
def compress_sb4x4(src, sb_idx, w, h, is_y):
    # hen ven gen
    if(is_y):
        if(sb_idx < w or ((sb_idx//w)%4) == 3):
            v_en = 0
        else:
            v_en = 1 
        if((sb_idx%w)==0 or (sb_idx%4)==0 ):
            h_en = 0
        else:
            h_en = 1 

    if(is_y==0):
        v_en = 0
        if((sb_idx%w)==0 or (sb_idx%2)==0) :
            h_en = 0
        else:
            h_en = 1 

    #print("hen" + str(h_en))
    #print("ven" + str(v_en))
    DC = [0, 0, 0, 0]
    left = [src[sb_idx-1][3],src[sb_idx-1][7],src[sb_idx-1][11],src[sb_idx-1][15]]

    has_left = h_en
    h_bits = compress(left,src[sb_idx],1,0,0, has_left,0)
    #h_bits = compress(left,[0]*16,1,0,0, has_left,0)

    #if(v_en==1):
        #top = [src[sb_idx-1][12],src[sb_idx-1][13],src[sb_idx-1][14],src[sb_idx-1][15]]
    has_top = v_en
    top = [src[sb_idx-1][12],src[sb_idx-1][13],src[sb_idx-1][14],src[sb_idx-1][15]]
    if(has_top and top[0] == src[sb_idx][0] and top[1] == src[sb_idx][1] and top[2]==src[sb_idx][2] and top[3]==src[sb_idx][3]):
        print("top: ")
        print(top)
        print("src: ")
        print(src[sb_idx])

    v_bits = compress(top,src[sb_idx],0,1,0, 0,has_top)

    #if(h_en==0 and v_en==0):
        #DC = [128,128,128,128]

    dc_bits = compress(DC,src[sb_idx],0,0,1,0,0)
    oth_bits = compress(DC, src[sb_idx], 0, 0, 0, 0, 0)


    #if(h_en==0 and v_en==0):
    #    min_bits = dc_bits
    #elif(h_en==1 and v_en==0):
    #    min_bits = h_bits
    #elif(h_en==0 and v_en==1):
    #    min_bits = v_bits
    #else:
    #min_bits = min(dc_bits,h_bits,v_bits,oth_bits)
    min_bits = min(dc_bits,h_bits,v_bits)
    #min_bits = dc_bits
    #min_bits = min(dc_bits,h_bits,v_bits)
    #min_bits = dc_bits
    if((min_bits%8) !=0 ):
        min_bits = (min_bits//8 + 1)*8

    return min_bits 



data=yuv_import(yuv_file,(width,height),1,1) #read yuv
YY=data[0][0]
im=PIL.Image.frombytes('L',(width,height),YY)
#im.show(YY)
im.save('a.jpg')





total_bits = 0
for i in range(0,sby_num):
    total_bits += compress_sb4x4(Ypixel,i,sbw,sbh,1)                              

print("Y total_bits" + (str)(total_bits) )

for i in range(0,sbuv_num):
    total_bits += compress_sb4x4(Upixel,i,sbw,sbh,0)                              

print(total_bits)

for i in range(0,sbuv_num):
    total_bits += compress_sb4x4(Vpixel,i,sbw,sbh,0)                              

print(total_bits)
ratio = total_bits/(width*height*8*1.5)
print("ratio:" + (str)(ratio))
print("copy num"+str(HV_copy_sbnum))
copy_ratio = HV_copy_sbnum/(sby_num+sbuv_num+sbuv_num)
print("HV copy ratio:" +(str)(copy_ratio) )




