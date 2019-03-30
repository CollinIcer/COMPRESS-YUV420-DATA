# COMPRESS-YUV420-DATA
This project is intend to test the lossless compress reference frame buffer in AVC codec/decode (HEVC is similar).
Compress Unit: 4x4 block
subblock_mode: 3 kinds, include 4x1、1x4、2x2, as follow:

Compress Element:
4bit K0:
     K0=0~8: the bits to represent the residual of 4 min vals of sublocks and the minest value of 4x4block
     K0=9: all bloack only has one pixel, now has another 8 bit to represent the pixel
     K0=10: this block is a copy of top 4x4 block
     K0=11: this block is a copy of left 4x4 block
2bit sb_mode:
     sb_mode = 0: 4x1
     sb_mode = 1: 1x4
     sb_mode = 2: 2x2
     sb_mode = 3: all 4x4 block is uncopress
     
 4bit K1:
     K1=0~8 :the bits to represent the residual of min vals of sublock and the other pixel in the sublock
     
 4bit K2:
     K2=0~8 :the bits to represent the residual of min vals of sublock and the other pixel in the sublock
     K2=9:  sublock2 is the same as sblock1
     
 4bit K3:
     K3=0~8 :the bits to represent the residual of min vals of sublock and the other pixel in the sublock
     K3=9:   sublock3 is the same as sblock1
     K3=10:  sublock3 is the same as sblock2
     
 4bit K4:
     K4=0~8 :the bits to represent the residual of min vals of sublock and the other pixel in the sublock
     K4=9:   sublock4 is the same as sblock1
     K4=10:  sublock4 is the same as sblock2
     K4=11:  sublock4 is the same as sblock3
     
 Total BITS COUNT:
     uncopress: K0 + sb_mode + 128 = 6 + 128
     block has same pixel: 4bit
     block copy top or left: 4bit
     others: as code,
     
        if(TR_COPY_MODE):
            k2_bits = 0 if((zero_cnt2==4) or ([src10,src11,src12,src13] == [src00,src01,src02,src03])) else (3*k2 + 2)
            k3_bits = 0 if((zero_cnt3==4) or ([src20,src21,src22,src23] == [src00,src01,src02,src03] or [src20,src21,src22,src23] == [src10,src11,src12,src13] )) else (3*k3 + 2)
            k4_bits = 0 if((zero_cnt4==4) or ([src30,src31,src32,src33] == [src00,src01,src02,src03] or [src30,src31,src32,src33] == [src10,src11,src12,src13]  or [src30,src31,src32,src33] == [src20,src21,src22,src23] )) else (3*k4 + 2)
        else:
            k2_bits = 0 if (zero_cnt2 == 4) else (3 * k2 + 2)
            k3_bits = 0 if (zero_cnt3 == 4) else (3 * k3 + 2)
            k4_bits = 0 if (zero_cnt4 == 4) else (3 * k4 + 2)

        bits = 30 + k0_bits + k1_bits + k2_bits + k3_bits + k4_bits 
        
    
