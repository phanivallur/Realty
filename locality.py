class Locality:
    def __init__(self,area,sqft_price,qbyq,trends,onebhk,twobhk,threebhk):
        self.area=area
        self.sqft_price=sqft_price
        self.qbyq=qbyq
        self.trends=trends
        self.onebhk=onebhk
        self.twobhk=twobhk
        self.threebhk=threebhk

    def __str__(self):
        return self.area+", "+self.sqft_price+", "+self.qbyq+", "+self.trends+", "+self.onebhk+", "+self.twobhk+", "+self.threebhk




