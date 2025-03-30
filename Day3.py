#Part1
def near_end_mul(s:str):
    return (mod_text.find(")")>0 and mod_text.find(")")<=11) and (mod_text.find(",")<mod_text.find(")"))

def cal_possible_mul(mul:str):
    multplers = mul[4:-1].split(",")
    if len(multplers)==2 and len(multplers[0]) <=3 and len(multplers[1]) <=3:
        try:
            return int(multplers[0])*int(multplers[1])
        except:
            return 0
    else:
        return 0    

with open('Day3_input.txt', 'r') as file:
    text = file.read()

mod_text = text
sum = 0
while (mod_text.find("mul(")+1):
    mod_text = mod_text[mod_text.find("mul("):]#see if there is a begining
    if near_end_mul(mod_text):#see if there is an end
        sum+=cal_possible_mul(mod_text[:mod_text.find(")")+1])
        mod_text = mod_text[mod_text.find(")"):]
    else:
        mod_text = mod_text[1:]#break the find_mul situation
print(sum) #182780583

#Part2
print(text.find("mul("))#5
print(text.find("do()"))#103
print(text.find("don't()"))#234
#the whole sequence start with an unclearified mul, seen as enabled mul
#1 add a situation judgement function return 0 after detected dont and 1 after do 
#2 add up the miscalculated mul and minus them from sum

#1
judg = 1

def check_enable(s:str):
    while (s.find("do()")+1) and (s.find("don't")+1):
        s = s[max([s.find("do()"),s.find("don't")]):]
    if s.find('do()')+1:
        globals()["judg"] = 1
    elif s.find("don't")+1:
        globals()["judg"] = 0
    return globals()["judg"]

mod_text = text
sum = 0
while (mod_text.find("mul(")+1):
    check_enable(mod_text[0:mod_text.find("mul(")]) # check the text between current and next mul
    mod_text = mod_text[mod_text.find("mul("):]
    if near_end_mul(mod_text):
        sum+=cal_possible_mul(mod_text[:mod_text.find(")")+1])*judg
        mod_text = mod_text[mod_text.find(")"):]
    else:
        mod_text = mod_text[1:]
print(sum) #90772405