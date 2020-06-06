class hun:   
    def __init__(self, ner: str, nas: int):       # байгуулагч функц үүсгэх
        self.ner = ner           
        self.nas = nas
        hun.too += 1  # объект дуудах бүрд нэгээр нэмэгдээд явна.
    def hi(self):           # гишүүн функц тодорхойлох
        print('Sain bna uu', self.ner, self.nas)
   
hun1 = hun('bold', 24 )
hun2 = hun('bayar', 22)
hun1.hi()
hun2.hi()
print(hun1.too)


