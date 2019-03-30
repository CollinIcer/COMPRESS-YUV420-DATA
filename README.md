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
     K1=0~8 :the bits to represent the residual of min vals of sublock and the other pixel in the sublock1
     k1=9   :sublock1 is the same as its left subblock in the same sb_mode
     k1=10  :sublock1 is the same as its top subblock in the same sb_mode
     
 4bit K2:
     K2=0~8 :the bits to represent the residual of min vals of sublock and the other pixel in the sublock2
     K2=9:   sublock2 is the same as its left subblock in the same sb_mode
     K2=10:  sublock2 is the same as its top subblock in the same sb_mode
     
 4bit K3:
     K3=0~8 :the bits to represent the residual of min vals of sublock and the other pixel in the sublock3
     K3=9:   sublock3 is the same as its left/top block's subblock in the same sb_mode
     K3=10:  sublock3 is the same as its sublock1
     K3=11:  sublock3 is the same as its sublock2
     
 4bit K4:
     K4=0~8 :the bits to represent the residual of min vals of sublock and the other pixel in the sublock4
     K4=9:   sublock4 is the same as its left/top block's subblock in the same sb_mode
     K4=10:  sublock4 is the same as sblock1
     K4=11:  sublock4 is the same as sblock2
     K4=12:  sublock4 is the same as sblock3
     
 Total BITS COUNT:
     uncopress: K0 + sb_mode + 128 = 6 + 128
     block has same pixel: 4bit
     block copy top or left: 4bit
     others: see in compress.py
     
        
        
    
