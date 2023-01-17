
###############################
# def fuct(n):
# 	if n <= 0:
# 		return 1
# 	else:
# 		return n * fuct(n-1)
#
#
# p = fuct(6)
# print(p)

################################ ПЕРЕБОР КАТАЛОГОВ И ФАЙЛОВ

F = {
	'C': {
		'Python39': ['python.exe', 'python.ini'],
		'Program files': {
			'Java': ['README.txt', 'Welcom.html', 'java.exe'],
			'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
		},
		'Windows': {
			'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
		}
	}
}

def get_files(path, depth=0):
	for f in path:
		print(" "*depth, f)
		if type(path[f]) == dict:
			get_files(path[f], depth +1)
		else:
			print(" "*(depth+1), " ".join(path[f]))


get_files(F)