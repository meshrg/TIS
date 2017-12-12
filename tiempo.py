import ntplib as ntp
import datetime
from time import ctime
from datetime import datetime
import ephem as ep


x = ntp.NTPClient()
c=x.request("mx.pool.ntp.org",version=4,timeout=5)

#ti=datetime.utcfromtimestamp(c.recv_time)
t1=ctime(c.recv_time)

t=datetime.utcfromtimestamp(c.recv_time)
da=datetime.date(t)



print t


print da

print type(da)

