import sys
import re

def main(args):
	state = False
	sum = 0

	general_regex = r'(on|off|=|\d+)'

	on_regex = r'on'
	off_regex = r'off'
	int_regex = r'\d+'
	equal_regex = r'='
	
	for line in sys.stdin:
		matches = re.findall(general_regex, line, re.I)

		for match in matches:
			
			if re.match(on_regex, match, re.I):
				state = True
			elif re.match(off_regex, match, re.I):
				state = False
			elif re.match(int_regex, match):
				if state:
					sum += int(match)
			elif re.match(equal_regex, match):
				print(f"Soma = {sum}")

		print(matches)

if __name__ == "__main__":
	main(sys.argv)
