from state import State
from state import idle
from state import moving
from lift import Lift
from transition import Transition


class system():
    max_=input("enter the maximum number of floors in the building:")
    lift1=Lift()
    lift1.curr_floor=0

    lift2=Lift()
    lift2.curr_floor=0
    i=0
    lift1_floor_value=[]
    lift2_floor_value=[]
    while i in range(max_):
        ele=0
        lift1_floor_value.append(ele)
        lift2_floor_value.append(ele)
        i=i+1


    def commander(self,system,lift1,lift2,lift1_floor_value,lift2_floor_value,max_):

        a=input("\nenter input :")
        pass_floor=a[0]
        direction=a[1]
        target_floor=a[2]

        a=pass_floor-lift1.curr_floor
        b=pass_floor-lift2.curr_floor

        if a*a>b*b:

            if direction=='U':
                if lift2.currentState==idle:
                    lift2.currentState=moving
                    system.upward(lift2.curr_floor,target_floor,lift2_floor_value,pass_floor,max_)

                else:
                    if lift2.dir=="up" & b>0:
                       system.upward(lift2.curr_floor,target_floor,lift2_floor_value,pass_floor,max_)

                    elif lift2.dir=="down" & b<0:
                        floor_number=pass_floor
                        if system.check_it(floor_number,lift1,lift2,direction,max_)==2:
                           system.downward(lift2.curr_floor,target_floor,lift2_floor_value,pass_floor,max_)
                        else:
                           system.downward(lift1.curr_floor,target_floor,lift1_floor_value,pass_floor,max_)

                    elif b==0:
                       system.upward(lift2.curr_floor,target_floor,lift2_floor_value,pass_floor,max_)

                    else:
                       system.downward(lift1.curr_floor,target_floor,lift2_floor_value,pass_floor,max_)

    def check_it(self,system,commander,floor_number,lift1,lift2,direction,max_):
        num1=floor_number
        num2=floor_number
        i=0
        if dir=='U':
            while i in range(floor_number):
                if lift1.floor_value[i]>0:
                    num1=i
                    break

                if lift2.floor_value[i]>0:
                    num2=i
                    break

            if num1>num2:
                return 1
            else:
                return 2

        else:
            while i in range(max_-floor_number):

                if lift1.floor_value[max_-i]>0:
                    num1=max_-i
                    break

                if lift2.floor_value[max_-i]>0:
                    num2=max_-i
                    break

            if num1<num2:
                return 1
            else:
                return 2

    def upward(self,Transition,commander,system,curr_floor,target_floor,floor_value,pass_floor,dir,max_):
        i=0
        while i in range(curr_floor,target_floor):
            prev_floor=curr_floor
            curr_floor=curr_floor+1
            i=i+1
            dir='up'
            print(prev_floor+"-->"+curr_floor+"\n")
            system.stop_decider(floor_value,pass_floor,target_floor,max_)
            if floor_value[curr_floor]>0:
                print("lift has stopped here"+"\n")
        system.commander()

    def downward(self,Transition,commander,system,curr_floor,target_floor,floor_value,pass_floor,dir,max_):
        j=0
        while j in range(curr_floor-target_floor,curr_floor):
            prev_floor=curr_floor 
            curr_floor=curr_floor-1  
            j=curr_floor
            dir='down'
            print(prev_floor+"-->"+curr_floor+"\n")
            system.stop_decider(floor_value,pass_floor,target_floor,max_)
            if floor_value[curr_floor]>0:
                print("lift has stopped here\n")
        system.commander()

    
    def stop_decider(self,system,commander,floor_value,pass_floor,target_floor,max_):
        num=1
        floor_value_writer(floor_value,pass_floor,num,max_)
        num=num+1
        floor_value_writer(target_floor,num,max_)

        def floor_value_writer(self,system,commander,floor_value,floor,num,max_):
            j=0
            while j in range(max_):
                if floor_value[j]:
                    floor_value[j]=floor_value[j]+1
                if j==floor:
                    floor_value[j]=floor_value[j]+num
                j=j+1





                    

