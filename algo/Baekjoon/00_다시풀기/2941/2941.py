grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']
n = ['ObjectOrientedProgramming1 3.0 A+', 'IntroductiontoComputerEngineering 3.0 A+', 'ObjectOrientedProgramming2 3.0 A0', 'CreativeComputerEngineeringDesign 3.0 A+', 'AssemblyLanguage 3.0 A+', 'InternetProgramming 3.0 B0', 'ApplicationProgramminginJava 3.0 A0', 'SystemProgramming 3.0 B0', 'OperatingSystem 3.0 B0',
     'WirelessCommunicationsandNetworking 3.0 C+', 'LogicCircuits 3.0 B0', 'DataStructure 4.0 A+', 'MicroprocessorApplication 3.0 B+', 'EmbeddedSoftware 3.0 C0', 'ComputerSecurity 3.0 D+', 'Database 3.0 C+', 'Algorithm 3.0 B0', 'CapstoneDesigninCSE 3.0 B+', 'CompilerDesign 3.0 D0', 'ProblemSolving 4.0 P']
r = []
s = []
# index를 사용하고 count를 사용해서grade index 기준으로 각 배열에 맞게 값을 생성..
# r.append(list(reversed(n[0])))
# print(n[0])

print(len(n))
for i in n:
    # ele = n[0]
    re_grade = i[::-1]
    score = re_grade[0:2:]
    re_score = score[::-1]
    # print()
    if re_score != ' P':
        r.append(re_score.replace(' ', ''))
    # r.append(grade.index('A+'))

for i in n:
    # ele = n[0]
    re_grade = i[::-1]
    score = re_grade[3:6:]
    re_score = score[::-1]
    if score[::-1] != '4.':
        s.append(re_score.replace(' ', ''))
    # r.append(grade.index('A+'))

print(s)
sum = 0
for ii in r:
    if ii == grade[0]:
        sum += 4.5
    elif ii == grade[1]:
        sum += 4.0
    elif ii == grade[2]:
        sum += 3.5
    elif ii == grade[3]:
        sum += 3.0
    elif ii == grade[4]:
        sum += 2.5
    elif ii == grade[5]:
        sum += 2.0
    elif ii == grade[6]:
        sum += 1.5
    elif ii == grade[7]:
        sum += 1.0
    elif ii == grade[8]:
        sum += 0.0
    # elif ii == grade[9]:
    #     sum += 0.0
# print(idx)
print(r)
print(sum)
print(sum/len(r))
# print(re_score)
# print(grade.index(re_score))
