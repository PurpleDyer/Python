a = int(input("Enter A Number: "))
sum_numbers = 0
for i in range(1, (a//2)+1):
    if a%i==0:
        sum_numbers += i

if sum_numbers == a:
    print("Addad Kamel Ast")
else:
    print("Addad Kamel Nist")

"""
int a = input()
sum_numbers = 0
for(int i = 1; i <= a//2; i += 1){
    if(a%i == 0){
        sum_numbers += i
    }
}
if (sum_numbers == a){
    print("Addad Kamel Ast")
}else{
    print("Addad Kamel Nist")
}
"""