class Database:
    @staticmethod
    def escape(value):
        return value.replace("'","''")

    @staticmethod
    def getConnection():
        return mysql.connector.connect(
            user='root',
            password='',
            host='127.0.0.1',
            database='users')

    @staticmethod
    def getResult(query,getOne=False):
        """Return a tuple of results or a single item (not in a tuple)
        """
        result_set=()
        conn = Database.getConnection()
        cur = conn.cursor()
        cur.execute(query)
        if getOne:
            result_set = cur.fetchone()
        else:
            result_set = cur.fetchall()
        cur.close()
        return result_set

    @staticmethod
    def doQuery(query):
        conn = Database.getConnection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        lastId = cur.lastrowid
        cur.close()

class Stocks:
    def __init__(self,id=0):
        self.stockName= ""
        self.stockSymbol= ""
        self.stockPrice= ""
        self.stockAvgVolume= ""
        self.stockRSI= ""
        self.stockSMA_50= ""
        self.stockSMA_200= ""
        # self.stockEarnings = ""  Definition: option 1: if stock beats earnings and guidance, option 2: stock doesn't beat earnings but beats guidance, option 3: stock beats earnings but not guidance, option 4: stock meets both, option 5: stock doesn't meet either.
        self.stockSentiment= ""

    def save(self):
        if self.id>0:
            return self.update()
        else:
            return self.insert()

    def insert(self):
        query = ("insert into users (firstname, lastname, company, email, username, password) values ('%s','%s','%s','%s','%s','%s')"%(Database.escape(self.firstname),Database.escape(self.lastname),Database.escape(self.company),self.email,self.username,self.password))
        Database.doQuery(query)
        return True

    def update(self):
        query = ("update users set (firstname, lastname, company, email, username, password) values ('%s','%s','%s','%s','%s','%s') where id=%d"%(Database.escape(self.firstname),Database.escape(self.lastname),Database.escape(self.company),self.email,self.username,self.password,self.id))
        Database.doQuery(query)
        return True


# Variables and Objectives
#
# stock name
# stock symbol
# stock price
# stock RSI over 3 month period
# stock 20 day SMA (% above/below)
# stock 50 day SMA (% above/below)
# stock 200 day SMA (% above/below)
# stock volume 20 day (% above/below)
# stock volume 50 day (% above/below)
# stock outsized day move (% above/below 2 std dev)
# stock earnings  1. Beat revenue, eps
#                 2. Beat eps
#                 3. Beat revenue
#                 4. Meets both
#                 5. Beats one, miss on the other
#                 6. Misses both
#
#                 1. Beats and raises guidance
#                 2. Beats guidance
#                 3. Meets guidance
#                 4. Misses
# stock dividend percentage (absolute and relative to peers) and any buyback programs in place
# stock sentiment 1. Analysts ratings (buy, sell, hold)
#                 2. Stock twits up/down
# stock leadership and vision (comparision against industry peers)
# us macro sentiment via federal reserve sentiment (fed fund futures) and rate picture, spy analysis and trend, usd 3 month trend
# world economy (china, japan, eu, uk) and world macro sentiment
#
# analyze for large moves, std. deviations away from norm are weighted heavier.
# adjust weights and biases through backtesting to create forecasts.
# choose about 20 widely held stocks and spy
#
# build lightweight react app (one page) to allow users to quickly parse through data and give analysis highlighting factors which are affecting stock price for both short and long term strategies
#
#
# sudo pip --no-cache-dir install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-linux_x86_64.whl
