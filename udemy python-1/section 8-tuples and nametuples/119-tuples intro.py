# t=("chetan",23,"sakoli","bhandara","maharashtra")

# name,age,city,dist,state=t
# print(t)

# name,_,city,dist,state=t
# name,*_,dist,state=t

# ts=[("Chetan",23),("Bhaurao",24),("samrit",25)]
# total_ages=0
# for i,items in enumerate(ts):

    # total_ages+=item[1]

    # print(f"{i}->{items}")

# print(total_ages)



# class emp:

#     def __init__(self,a,b) :
        
#         self.a=a
#         self.b=b

#     def __repr__(self) :

#         return (f"{self.__class__.__name__}{(self.a,self.b)}")


# obj=emp(2,3)
# print(obj)
# print(id(obj))
# obj.a=4
# print(obj)
# print(id(obj))


t=(2,3,4,5)

print(t,id(t))

t+=(0,4)

print(t,id(t))

            