#!/usr/bin/python

from PIL import Image
import string, argparse

def main():
	parser = argparse.ArgumentParser(description='Convert image to thingy')
	parser.add_argument('input', type=str, help='Input image file')
	parser.add_argument('output', type=str, help='Output file')
	parser.add_argument(
		'--width', type=int, default=80, help='Image width (default:80)')
	parser.add_argument(
		'--height', type=int, default=60, help='Image height (default:60)')
	args = parser.parse_args()
	
	input_pic = Image.open(args.input).convert('RGBA')
	pic_pixels = input_pic.load()
	
	output_pic = open(args.output,'w')
	
	for y in range(args.height):
		for x in range(args.width):
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
			
			output_pic.write(''.join((
				string.hexdigits[upper_nibble],
				string.hexdigits[lower_nibble],
				' '
			)))
	
	output_pic.close()
	
if __name__ == '__main__':
	main()
