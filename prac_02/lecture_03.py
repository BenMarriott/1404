reg_days, fast_days = 4, 3
meat_normal = .850 * reg_days
meat_fast = .650 * fast_days
total_meat = meat_fast + meat_normal
steph_norm = .450 * 4
steph_fast = .300 * 3
steph_total = steph_fast + steph_norm
user = input("Ben or Steph?").capitalize()
while user == "Ben":
    print("For 1 week of normal days Ben need {}kg's of meat & for fasting days; {:.2f}kg's. Total meat required for 1 week is: {}kg's of meat".format(
        meat_normal, meat_fast, total_meat))
    user = input("Ben or Steph?").upper
else:
    print("For 1 week of normal days Steph need {}kg's of meat & for fasting days; {:.2f}kg's. Total meat required for 1 week is: {}kg's of meat".format(
            steph_norm, steph_fast, steph_total+.150))
    user = input("Ben or Steph?").upper




#norm = 450
# fast = 300
#+ 150