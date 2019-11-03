print(
True and True,"\n", #T
False and True,"\n", #F
1 == 1 and 2 == 1,"\n", #F
"test" == "test","\n", #T
1 == 1 or 2 != 1,"\n", #T
True and 1 == 1,"\n", #T
False and 0 != 0,"\n", #F
True or 1 == 1,"\n", #T
1 != 0 and 2 == 1,"\n", #F
"test" == "testing","\n", #F
"test" == 1,"\n", #F
not (True and False),"\n", #T
not (1 == 1 and 0 != 1),"\n", #F
not (10 == 1 or 1000 == 1000),"\n", #F
not (1 != 10 or 3 == 4),"\n", #F
not ("testing" == "testing" and "Zed" == "Cool Guy"),"\n", #T
1 == 1 and not ("testing" == 1 or 1 == 0),"\n", #T
"chunky" == "bacon" and not (3 == 4 or 3 == 3),"\n", #F
3 == 3 and not("testing" == "testing" or "Python" == "Fun") #F
)