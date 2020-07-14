#!/usr/bin/python

from PIL import Image
import string, argparse, itertools

def main():
	parser = argparse.ArgumentParser(description='Convert image to thingy')
	
	parser.add_argument('input' , type=str, help='Input image file')
	parser.add_argument('output', type=str, help='Output file')
	parser.add_argument(
		'--width' , type=int, default=80, help='Image width  (default:80)')
	parser.add_argument(
		'--height', type=int, default=60, help='Image height (default:60)')
		
	args = parser.parse_args()
	
	pic_pixels = Image.open(args.input).convert('RGB').load()
	
	with open(args.output, 'w') as output_pic:
		for y, x in itertools.product(range(args.height), range(args.width)):
			pixel = pic_pixels[x,y]
			byte_out = (
				((pixel[0] & 0b11100000) >> 5) |
				((pixel[1] & 0b11100000) >> 2) |
				((pixel[2] & 0b11000000)     )
			)

			output_pic.write(''.join((
				string.hexdigits[(byte_out & 0b11110000) >> 4],
				string.hexdigits[(byte_out & 0b00001111)     ], ' '
			)))
	
if __name__ == '__main__':
	main()
