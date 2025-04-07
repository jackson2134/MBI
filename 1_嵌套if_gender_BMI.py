user_name=input("请输入您的名字：")
user_gender=input("请输入您的性别（男/女）：")
user_weight=input("请输入您的体重，单位kg(仅输入数字)：")
user_hight=input("请输入您的身高，单位m：(仅输入数字)：")
# user_weight_str=str(user_weight)
user_weight_int=int(user_weight)
user_hight_float=float(user_hight)
# print("您的体重为: "+user_weight+"kg")
# print("您的身高为: "+user_weight+"m")
BMI=user_weight_int/user_hight_float**2
BMI_str=str(BMI)# BMI=体重/身高**2
print('您的BMI为： '+BMI_str)
# 以上代码用来计算BMI
if BMI<18.5:
    if user_gender=="男":
        print(user_name+"先生，您的体重有点低，为了您的身体健康，请合理饮食")
    else:#user_gender=女
        print(user_name+"女士，您的体重有点低，为了您的身体健康，请合理饮食")
elif 24>BMI>=18.5:
    if user_gender=="男":
        print(user_name+"先生，你的体重处于正常水平，请继续保持")
    else:#user_gender=女
        print(user_name+"女士，你的体重处于正常水平，请继续保持")
elif 28>BMI>=24:
    if user_gender=="男":
        print(user_name+"先生，您有些超重，为了您的身体健康，请饮食清淡，多吃蔬菜水果")
    else:#user_gender=女
        print(user_name+"女士，您有些超重，为了您的身体健康，请饮食清淡，多吃蔬菜水果")
elif 32.5>BMI>=28:
    if user_gender=="男":
        print(user_name+"先生，你处于轻度肥胖阶段，为了您的身体健康，请合理饮食，并适当进行体育锻炼")
    else:#user_gender=女
        print(user_name+"女士，你处于轻度肥胖阶段，为了您的身体健康，请合理饮食，并适当进行体育锻炼")
elif 37.5>BMI>=32.5:
    if user_gender=='男':
        print(user_name+"先生，你处于中度肥胖阶段，为了您的身体健康，请合理饮食，并适当进行体育锻炼")
    else:#user_gender=女
        print(user_name+"女生，你处于中度肥胖阶段，为了您的身体健康，请合理饮食，并适当进行体育锻炼")
elif 50>BMI>=37.5:
    if user_gender=='男':
        print(user_name+"先生，你处于重度肥胖阶段，为了您的身体健康，请合理饮食，并适当进行体育锻炼，必要时寻求医生帮助")
    else:#user_gender=女
        print(user_name+"女士，你处于重度肥胖阶段，为了您的身体健康，请合理饮食，并适当进行体育锻炼，必要时寻求医生帮助")
else:
    if user_gender=='男':
        print(user_name+"先生，你处于极重度肥胖阶段，为了您的身体健康，请合理饮食，并适当进行体育锻炼，必要时寻求医生帮助")
    else:#user_gender=女
        print(user_name+"女士，你处于极重度肥胖阶段，为了您的身体健康，请合理饮食，并适当进行体育锻炼，必要时寻求医生帮助")