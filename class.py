

class hun:   
    def __init__(self, ner: str, nas: int):       # байгуулагч функц тодорхойлох
        print('constructor duudagdaw... ')

    def __del__(self):         #  устгагч функц тодорхойлох
        print('destructor duudagdaw')

hun1 = hun('bold', 24 )
hun2 = hun('bayar', 22)


too = 15  # static өгөгдөл  дундаа ашиглана