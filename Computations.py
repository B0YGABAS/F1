class Computations():
    def __init__(self):
        pass

    def get_total_wear(self,driver_tyre):
        driver={}
        for i,j in driver_tyre.items():
            driver[i]=sum(j.values())/len(j)
        return driver

# a=Computations()
# print(a.get_total_wear({1:{"RL":50,"RR":40,"FL":30,"FR":20},2:{"RL":20,"RR":42,"FL":12,"FR":90}}))