""" Get bond price from YTM """
def bond_price(par, T, ytm, coup, freq):
    freq = float(freq)
    periods = T*freq
    coupon = coup/100.*par/freq
    print(coupon)
    dt = [(i+1)/freq for i in range(int(periods))]
    price = sum([coupon/(1+ytm/freq)**(freq*t) for t in dt]) + \
            par/(1+ytm/freq)**(freq*T)
    return price


