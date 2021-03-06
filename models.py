from app import db

class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10))
    name = db.Column(db.String())
    exchange = db.Column(db.String())

    def __init__(self, symbol, name, exchange):
        self.symbol = symbol,
        self.name = name,
        self.exchange = exchange,

    def __repr__(self):
        s = '<Symbol: %(1)s, Name: %(2)s, Exchange: %(3)s>'
        print(s)
        return s % {"1" : self.symbol, "2" : self.name, "3" : self.exchange}


class Quote(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10))
    name = db.Column(db.String(), unique=True)
    change = db.Column(db.Float())
    changePercent = db.Column(db.Float())
    timestamp = db.Column(db.String())
    volume = db.Column(db.Integer())
    changeYTD = db.Column(db.Float())
    changeYTDPercent = db.Column(db.Float())
    high = db.Column(db.Float())
    low = db.Column(db.Float())
    open = db.Column(db.Float())

    def __init__(self, symbol, name, change, changePercent, timestamp,
                 volume, changeYTD, changeYTDPercent, high, low, open):
        self.symbol = symbol
        self.name = name
        self.change = change
        self.changePercent = changePercent
        self.timestamp = timestamp
        self.volume = volume
        self.changeYTD = changeYTD
        self.changeYTDPercent = changeYTDPercent
        self.high = high
        self.low = low
        self.open = open

    def __repr__(self):
        s = '<Open: %(1)f, High: %(2)f, Close: %(3)f>'
        return s % {"1" : self.open, "2" : self.high, "3" : self.close}

