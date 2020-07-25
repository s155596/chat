# 讀取檔案
def read_file(filename): 
	lines = []
	with open(filename,'r', encoding='utf-8-sig') as f: # 加'-sig'是指把'\ufeff'去掉
		for line in f:
			lines.append(line.strip()) # strip 為把line內的\n拿掉
	return lines # 把lines清單提出來

# 文字轉換
def convert(lines): # 把lines清單傳進來
	new = []
	person = None # Python的語法, 即'無'
	for line in lines:
		if line == 'Allen':
			person = 'Allen' # 把現在說話的人存成Allen
			continue # 跳到下一個迴圈, 會保留Person為Allen, ˊ只是new.append語法不執行
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # 
			new.append(person + ':' + line)
	return new

def write_file(filename, lines): # 讀取裝著對話紀錄的清單
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main(): # 寫主程式
	lines = read_file('input.txt') # 使用此function才把input.txt打開
	lines = convert(lines) # 覆蓋的感覺
	write_file('output.txt', lines)

main() # 程式的進入點