#Author - SHIVAM KUMAR

#here the inputs are fixed that is  '0' and '1'

def equivalence(inp0, inp1, cequi, l):

	nequi = []

	temp = []
	#l.remove(finals)
	#print(l)
	#print(cequi)
	a = 0
	for i in l:

		pos0 = 0
		pos1 = 0

		for j in range(len(cequi)):

			if inp0[i] in cequi[j]:
				pos0 = j
				break

			else:
				continue
		for j in range(len(cequi)):

			if inp1[i] in cequi[j]:
				pos1 = j
				break

			else:
				continue
		#print(i, " pos0 = ",pos0," pos1 = ", pos1)

		a = 0

		for k in range(len(nequi)):
			st = nequi[k][0]

			if(inp1[st] in cequi[pos1]) and (inp0[st] in cequi[pos0]):
				(nequi[k]).append(i)
				a = 1
				break

		if(a == 0):
			temp = []
			temp.append(i)
			nequi.append(temp)
			#print(i,"nequi in function = ", nequi)


	if(a == 1):
		#nequi.append(temp)
		pass


	#print("in funtion nequi = ",nequi)


	"""
	for i in nequi:
		if(i not in nnequi):
			nnequi.append(i)
	temp.append(finals)
	nnequi.append(finals)

	temp = []
	temp.append(finals)
	nequi.append(temp)

	"""
	return nequi







def dfaminimization(n, inp0, inp1, l, finallist):

	cequi = []
	temp = []
	#temp.append(finals)

	temp = []
	nequi = []
	count = 0;
	for i in range(len(l)):
		temp.append(l[i])

	cequi.append(temp)
	cequi.append(finallist)

	print()
	print(0, " equivalence ", cequi)

	m = 0
	nequi = equivalence(inp0, inp1, cequi,l)
	temp = equivalence(inp0, inp1, cequi, finallist)
	for elem in temp:
		nequi.append(elem)



	for i in range(1, 2 ** n):
		print()
		print(i," equivalence ", nequi)
		if nequi == cequi:
			m = 1
			print()
			print("The minimization of above given DFA is ",i-1," equivalence ",nequi)
			break

		else:
			cequi = nequi
			nequi = equivalence(inp0, inp1, cequi, l)
			temp = equivalence(inp0, inp1, cequi, finallist)
			for elem in temp:
				nequi.append(elem)





	if(m == 0):
		print()
		print("The minimization of above given DFA is ",(2 * n) -1, " equivalence ", nequi)






def printintialstates(n, inp0, inp1, l, finallist, initiallist):
	print("i-> denotes intial state and f-> denotes final states")
	print()
	print(" states    input 0    input 1")

	for i in range(len(l)):
		print()
		if i in initiallist:
			print("i->",l[i],"      ",inp0[l[i]],"      ",inp1[l[i]])

		else:
			print("   ",l[i],"      ",inp0[l[i]],"      ",inp1[l[i]])

	for finals in finallist:
		print()
		print("f->",finals,"      ",inp0[finals],"      ",inp1[finals])



n = int(input("enter no of states \n"))
inp0 = {}
inp1 = {}
states = []

for i in range(n):
	print(" enter  state    enter the state when intial state accepts the input 0    enter the state when intial state accepts 1 ")
	q = input()
	states.append(q)
	q0 = input()
	q1 = input()
	inp0[q] = q0
	inp1[q] = q1

#total no of initial states
print()
noi = int(input("enter total no of initial states \n"))
initiallist = []
for i in range(noi):
	print()
	initial = input("enter the state which is initial from above states you have entered  \n")

	initiallist.append(initial)

#total no of final states
print()
nof = int(input("enter total no of final states "))
finallist = []
for i in range(nof):
	print()
	finals = input("enter the state which is final from above states you have entered \n")
	states.remove(finals)
	finallist.append(finals)

print()
printintialstates(n, inp0, inp1, states, finallist, initiallist)

#to remove unreachable states
state = []
for i in states:

	if (i not in list(inp0.values())) and (i not in list(inp1.values())) and i not in initiallist:
		print()
		print(i," is unreachable state ")
		continue
	else:
		state.append(i)


#to minimize DFA
dfaminimization(n, inp0, inp1, state, finallist)
