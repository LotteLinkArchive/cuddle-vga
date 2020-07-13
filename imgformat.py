#!/usr/bin/python

from PIL import Image

hexchars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

def main():
	
	input_pic = Image.open('pic.png')
	output_string = ''
	pic_pixels = input_pic.load()
	
	for y in range(60):
		for x in range(80):
			pixel = pic_pixels[x,y]
			byte_out = 0
			
			col_r = pixel[0] & 0b11100000
			col_r >>= 5
			byte_out |= col_r
			
			col_g = pixel[1] & 0b11100000
			col_g >>= 2
			byte_out |= col_g
			
			col_b = pixel[2] & 0b11000000
			byte_out |= col_b
			
			upper_nibble = byte_out & 0b11110000
			upper_nibble >>= 4
			lower_nibble = byte_out & 0b00001111
			
			ascii_out = hexchars[upper_nibble] + hexchars[lower_nibble]
			output_string += ascii_out + ' '
	
	
	del input_pic
	
	output_pic = open('pic.txt','wb')
	output_pic.write(output_string)
	output_pic.close()
	
if (__name__=='__main__'):
	main()
