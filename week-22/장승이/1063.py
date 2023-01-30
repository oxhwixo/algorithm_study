# 1063 킹
# 실버 3

dic = {'R':[0, 1], 'L':[0, -1], 'B':[-1, 0], 'T':[1, 0],\
	'RT':[1, 1], 'LT':[1, -1], 'RB':[-1, 1], 'LB':[-1, -1]}

king, rock, n = input().split()
n = int(n)
moves = [input() for i in range(n)]

kx, ky = int(king[1]) - 1, ord(king[0]) - ord('A')
rx, ry = int(rock[1]) - 1, ord(rock[0]) - ord('A')

for i in range(n):
	move = dic[moves[i]]
	next_kx, next_ky = kx + move[0], ky + move[1]
	
	if next_kx < 0 or next_ky < 0 or next_kx > 7 or next_ky > 7:
		continue

	elif next_kx == rx and next_ky == ry:
		next_rx, next_ry = rx + move[0], ry + move[1]

		if next_rx < 0 or next_ry < 0 or next_rx > 7 or next_ry > 7:
			continue
		else:
			kx, ky = next_kx, next_ky
			rx, ry = next_rx, next_ry
	
	else:
		kx, ky = next_kx, next_ky

print(chr(ord('A') + ky)+str(kx+1))
print(chr(ord('A') + ry)+str(rx+1))
