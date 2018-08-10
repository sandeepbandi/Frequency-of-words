import hashlib
import datetime

class Block(object):

	def __init__(self,index,timestamp,data,hash):
		self.index=index
		self.timestamp=datetime.datetime.now()
		self.data=data
		self.hash=self._generate_hash(index,timestamp,data)

	def _generate_hash(self,index,timestamp,data):
		encode = data.encode('utf-8')
		encode_int = repr(index).encode('utf-8')
		data_encode = hashlib.sha256(encode).digest()
		int_encode = hashlib.sha256(encode_int).digest()
		encode_date = repr(timestamp).encode('utf-8')
		date_en = hashlib.sha256(encode_date).digest()
		return date_en,int_encode,data_encode

obj = Block(1,datetime.datetime.now(),'Im sandeep',hash)


def genesis_block(index,data,timestamp):
	return index,data,timestamp

# print genesis_block(0,"genesis block",datetime.datetime.now())

func = genesis_block(0,'genesis block',datetime.datetime.now())

def next_block(fun):
	index=func[0]+1       #here I took genesis_block as the 'last_block' and gensis_block index
	data = func[1] + ' ' + "next block" #gensis_block data
	timestamp = datetime.datetime.now()
	hash = obj._generate_hash(index,timestamp,data)
	return hash,data_new,ab

print next_block(fun)