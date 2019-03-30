# -*- coding: utf-8 -*-
 
from numpy import *
import PIL.Image 
screenLevels = 255.0
#4x4 pixel


TR_COPY_MODE = 1 
SB_COPY_MODE = 1  
SUBBLOCK_MODE  = 1 #3 sub block
#yuv_file = "test1280x720.yuv"
yuv_file = "vid720.yuv"
#yuv_file = "vid00_720.yuv"
width = 1280
height = 720

#yuv_file = "test640x480.yuv"
#width = 640
#height = 480

#yuv_file = "test160x160.yuv"
#width = 160
#height = 160

#yuv_file = "test1024x768.yuv"
#width = 1024 
#height = 768 

#yuv_file = "test320x240.yuv"
#width = 320 
#height = 240 


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
uncompress_sbnum =0


def yuv_import(filename,dims,numfrm,startfrm):
    fp=open(filename,'rb')
    #print(prod(dims))
    blk_size = (dims[0] * dims[1]*3/2)
    seek_len = (int)(blk_size*startfrm)
    #print(seek_len)
    fp.seek(seek_len,0)
    y_w =dims[0]  
    y_h =dims[1]
    uv_w=dims[0]//2
    uv_h=dims[1]//2
    Yt=zeros((y_h,y_w),uint8,'C')
    Ut=zeros((uv_h,uv_w),uint8,'C')
    Vt=zeros((uv_h,uv_w),uint8,'C')
    for i in range(numfrm):
        for m in range(y_h):  # y dirc
            for n in range(y_w):# x dirc
                Yt[m, n] = int.from_bytes(fp.read(1), byteorder='little', signed=False)
               #print( Yt[m, n] )
        for m in range(uv_h):
            for n in range(uv_w):
                Ut[m, n] = int.from_bytes(fp.read(1), byteorder='little', signed=False)
        for m in range(uv_h):
            for n in range(uv_w):
                Vt[m, n] = int.from_bytes(fp.read(1), byteorder='little', signed=False)


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
           
            Ypixel[idx+idy*sbw] = [Yt[newy0,newx], Yt[newy0,newx+1], Yt[newy0,newx+2], Yt[newy0,newx+3], 
                                   Yt[newy1,newx], Yt[newy1,newx+1], Yt[newy1,newx+2], Yt[newy1,newx+3],   
                                   Yt[newy2,newx], Yt[newy2,newx+1], Yt[newy2,newx+2], Yt[newy2,newx+3],  
                                   Yt[newy3,newx], Yt[newy3,newx+1], Yt[newy3,newx+2], Yt[newy3,newx+3]]

            #print("sbidx"+str(idx+idy*sbw))
            #print(Ypixel[idx+idy*sbw])


    for idy in range(uv_sbh):
        for idx in range(uv_sbw):
            newx = idx*4+0   
            newy0 = (idy*4+0) 
            newy1 = (idy*4+1) 
            newy2 = (idy*4+2) 
            newy3 = (idy*4+3) 
            Upixel[idx+idy*uv_sbw] = [Ut[newy0,newx], Ut[newy0,newx+1], Ut[newy0,newx+2], Ut[newy0,newx+3],
                                      Ut[newy1,newx], Ut[newy1,newx+1], Ut[newy1,newx+2], Ut[newy1,newx+3],
                                      Ut[newy2,newx], Ut[newy2,newx+1], Ut[newy2,newx+2], Ut[newy2,newx+3],
                                      Ut[newy3,newx], Ut[newy3,newx+1], Ut[newy3,newx+2], Ut[newy3,newx+3]]



            #print("usbidx"+str(idx+idy*uv_sbw))
            #print(Upixel[idx+idy*uv_sbw])
   	
    for idy in range(uv_sbh):
        for idx in range(uv_sbw):
            newx = idx*4+0   
            newy0 = (idy*4+0) 
            newy1 = (idy*4+1) 
            newy2 = (idy*4+2) 
            newy3 = (idy*4+3) 
   	
            Vpixel[idx+idy*uv_sbw] = [Vt[newy0,newx], Vt[newy0,newx+1], Vt[newy0,newx+2], Vt[newy0,newx+3],
                                      Vt[newy1,newx], Vt[newy1,newx+1], Vt[newy1,newx+2], Vt[newy1,newx+3],
                                      Vt[newy2,newx], Vt[newy2,newx+1], Vt[newy2,newx+2], Vt[newy2,newx+3],
                                      Vt[newy3,newx], Vt[newy3,newx+1], Vt[newy3,newx+2], Vt[newy3,newx+3]]



            #print("vsbidx"+str(idx+idy*uv_sbw))
            #print(Vpixel[idx+idy*uv_sbw])


		
    fp.close()
    return (Yt,Ut,Vt)
	
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
        src00 = src[0]   
        src01 = src[1]   
        src02 = src[2]   
        src03 = src[3]   
        
        src10 = src[4]   
        src11 = src[5]   
        src12 = src[6]   
        src13 = src[7]   

        src20 = src[8 ]  
        src21 = src[9 ]  
        src22 = src[10]  
        src23 = src[11]  

        src30 = src[12]  
        src31 = src[13]  
        src32 = src[14]  
        src33 = src[15]  


    elif(is_v):
        src00 = src[0]   
        src01 = src[4]   
        src02 = src[8]   
        src03 = src[12]  
        
        src10 = src[1]   
        src11 = src[5]   
        src12 = src[9]   
        src13 = src[13]  

        src20 = src[2 ]  
        src21 = src[6 ]  
        src22 = src[10]  
        src23 = src[14]  

        src30 = src[3]   
        src31 = src[7]   
        src32 = src[11]  
        src33 = src[15]  

    elif(is_dc):
        src00 = src[0]   
        src01 = src[1]   
        src02 = src[4]   
        src03 = src[5]   

        src10 = src[2]   
        src11 = src[3]   
        src12 = src[6]   
        src13 = src[7]   

        src20 = src[8]   
        src21 = src[9]   
        src22 = src[12]  
        src23 = src[13]  

        src30 = src[10]  
        src31 = src[11]  
        src32 = src[14]  
        src33 = src[15]  

    else:
        src00 = src[0]  
        src01 = src[1]  
        src02 = src[2]  
        src03 = src[3]  

        src10 = src[4]  
        src11 = src[5]  
        src12 = src[8]  
        src13 = src[9]  

        src20 = src[6]  
        src21 = src[7]  
        src22 = src[10] 
        src23 = src[11] 

        src30 = src[12] 
        src31 = src[13] 
        src32 = src[14] 
        src33 = src[15] 

    global HV_copy_sbnum
    global uncompress_sbnum

    
    if( SB_COPY_MODE and src == pred and ( (has_left and is_h) or (has_top and is_v) ) ): 
        #print("v H copy mode")
        HV_copy_sbnum +=1
        return 4 #B_K0  

    #print("is_h,isv :"+str(is_h) + " " + str(is_v))
    #print(src00,src01,src02,src03)
    #print(src10,src11,src12,src13)
    #print(src20,src21,src22,src23)
    #print(src30,src31,src32,src33)



    #if([src00,src01,src02,src03,src10,src11,src12,src13,src20,src21,src22,src23,src30,src31,src32,src33] == ([0]*16)):
    #   HV_copy_sbnum+=1
    #   print("copy ")
    #    return 0
    #else:
    min0 = min(src00,src01,src02,src03)
    min1 = min(src10,src11,src12,src13)
    min2 = min(src20,src21,src22,src23)
    min3 = min(src30,src31,src32,src33)

    min_tr = min(min0,min1,min2,min3)

    min_src0 = min0 - min_tr
    min_src1 = min1 - min_tr
    min_src2 = min2 - min_tr
    min_src3 = min3 - min_tr
 
    min_src_max = max(min_src0,min_src2,min_src2,min_src3)
        
    src0_sub_max = max(src00-min0,src01-min0,src02-min0,src03-min0)
    src1_sub_max = max(src10-min1,src11-min1,src12-min1,src13-min1)
    src2_sub_max = max(src20-min2,src21-min2,src22-min2,src23-min2)
    src3_sub_max = max(src30-min3,src31-min3,src32-min3,src33-min3)


    k0 = get_bits(min_src_max)
    k1 = get_bits(src0_sub_max)
    k2 = get_bits(src1_sub_max)
    k3 = get_bits(src2_sub_max)
    k4 = get_bits(src3_sub_max)

    #zero_cnt0 = (int)(min_src0==0) + (int)(min_src1==0) + (int)(min_src2==0) + (int)(min_src3==0)
    #zero_cnt1 = (int)(src00==min0) + (int)(src01==min0) + (int)(src02==min0) + (int)(src03==min0)
    #zero_cnt2 = (int)(src10==min1) + (int)(src11==min1) + (int)(src12==min1) + (int)(src13==min1)
    #zero_cnt3 = (int)(src20==min2) + (int)(src21==min2) + (int)(src22==min2) + (int)(src23==min2)
    #zero_cnt4 = (int)(src30==min3) + (int)(src31==min3) + (int)(src32==min3) + (int)(src33==min3)

    zero_cnt0 = zero_cnt([min_src0,min_src1,min_src2,min_src3])
    zero_cnt1 = zero_cnt([src00-min0,src01-min0,src02-min0,src03-min0])
    zero_cnt2 = zero_cnt([src10-min1,src11-min1,src12-min1,src13-min1])
    zero_cnt3 = zero_cnt([src20-min2,src21-min2,src22-min2,src23-min2])
    zero_cnt4 = zero_cnt([src30-min3,src31-min3,src32-min3,src33-min3])

    #print("zero " + (str)(zero_cnt0)  + " "  + (str)(zero_cnt1) + " " + (str)(zero_cnt2) + " " + (str)(zero_cnt3) + " " + (str)(zero_cnt4))
    
    #bits = 28 + 4*(k0+k1+k2+k3+k4)
    #bits = 28 + (4-zero_cnt0)*k0 + (4-zero_cnt1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
    #bits = 28 + 4*k0 + (4-zero_cnt1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
    if(zero_cnt0==4 and zero_cnt1==4 and zero_cnt2==4 and zero_cnt3==4 and zero_cnt4==4):
        bits = 8+4 #B_K0 + min_val
        #print("all pixel is the same in the 4x4 block")
        
    else:
        #bits = 28 + (4-zero_cnt0)*k0 + (4-zero_cnt1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
        #bits = 30 + (4-zero_cnt0)*k0 + (4-zero_cnt1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
        k0_bits = 0 if(zero_cnt0==4) else (3*k0 + 2)
        k1_bits = 0 if(zero_cnt1==4) else (3*k1 + 2)

        if(TR_COPY_MODE):
            k2_bits = 0 if((zero_cnt2==4) or ([src10,src11,src12,src13] == [src00,src01,src02,src03])) else (3*k2 + 2)
            k3_bits = 0 if((zero_cnt3==4) or ([src20,src21,src22,src23] == [src00,src01,src02,src03] or [src20,src21,src22,src23] == [src10,src11,src12,src13] )) else (3*k3 + 2)
            k4_bits = 0 if((zero_cnt4==4) or ([src30,src31,src32,src33] == [src00,src01,src02,src03] or [src30,src31,src32,src33] == [src10,src11,src12,src13]  or [src30,src31,src32,src33] == [src20,src21,src22,src23] )) else (3*k4 + 2)
        else:
            k2_bits = 0 if (zero_cnt2 == 4) else (3 * k2 + 2)
            k3_bits = 0 if (zero_cnt3 == 4) else (3 * k3 + 2)
            k4_bits = 0 if (zero_cnt4 == 4) else (3 * k4 + 2)

        #bits = 30 + (4-zero_cnt0)*k0 + (4t1)*k1 +  (4-zero_cnt2)*k2 + (4-zero_cnt3)*k3 + (4-zero_cnt4)*k4
        bits = 30 + k0_bits + k1_bits + k2_bits + k3_bits + k4_bits 
        #print("k0,k1,k2,k3,k4 " + str(k0_bits) + " " + str(k1_bits) + " " + str(k2_bits) + " " + str(k3_bits) + " " + str(k4_bits))
    if(bits<128):
        return bits
    else:
        uncompress_sbnum +=1
        return 128 + 6 

	
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
    has_left = h_en
    left=[0]*16
    if(has_left):
        left = src[sb_idx-1]

    has_top = v_en
    top = [0]*16
    if(has_top):
        top = src[sb_idx-w]

    #print("\n src \n")
    #print(src[sb_idx])
    #if(has_left): 
    #    print("\n left \n")
    #    print(left)
    #if(has_top):
    #    print("\n top \n")
    #    print(top)


    h_bits = compress(left,src[sb_idx],1,0,0, has_left,0)
    v_bits = compress(top,src[sb_idx],0,1,0, 0,has_top)
    dc_bits = compress(DC,src[sb_idx],0,0,1,0,0)
    #oth_bits = compress(DC, src[sb_idx], 0, 0, 0, 0, 0)

    if(SUBBLOCK_MODE):
        min_bits = min(dc_bits,h_bits,v_bits)
    else:
        min_bits = dc_bits-2
    #min_bits = dc_bits
    #min_bits = min(dc_bits,h_bits,v_bits)
    #if((min_bits%8) !=0 ):
    #    min_bits = (min_bits//8 + 1)*8

    return min_bits 


for frame in range(0,10): #10 frame num
    data=yuv_import(yuv_file,(width,height),1,frame) #read yuv
    YY=data[0]
    im=PIL.Image.fromarray(YY,'L')
    #im.show(YY)
    save_file = "pic"+str(frame)+".jpg"
    im.save(save_file)
    
    total_bits = 0
    HV_copy_sbnum = 0
    uncompress_sbnum = 0
    #total_bits += compress_sb4x4(Ypixel,0,sbw,sbh,1)
    for i in range(0,sby_num):
        total_bits += compress_sb4x4(Ypixel,i,sbw,sbh,1)
    #
    print("Y total_bits" + (str)(total_bits) )
    #
    for i in range(0,sbuv_num):
        total_bits += compress_sb4x4(Upixel,i,uv_sbw,uv_sbh,0)
    #
    #print(total_bits)
    for i in range(0,sbuv_num):
        total_bits += compress_sb4x4(Vpixel,i,uv_sbw,uv_sbh,0)
    #
    #print(total_bits)
    ratio = total_bits/(width*height*8*1.5)
    print("frame: " + str(frame))
    print("ratio:" + (str)(ratio))
    print("HV COPY sblock num : " + str(HV_copy_sbnum))
    print("uncopress sblock num : " + str(uncompress_sbnum))
