class FRController:
    def __init__(self): self.fwd=False; self.rev=False
    def stop(self): self.fwd=self.rev=False
    def start_fwd(self):
        if not self.rev: self.fwd=True
    def start_rev(self):
        if not self.fwd: self.rev=True
    def valid(self): return not (self.fwd and self.rev)

class StarDelta:
    def state(self,t):
        main=t>=0
        star=0<=t<3.0
        dead=3.0<=t<3.2
        delta=t>=3.2
        assert not (star and delta)
        return main,star,dead,delta

c=FRController(); c.start_fwd(); c.start_rev(); print('FWD/REV=',c.fwd,c.rev,'valid=',c.valid()); c.stop(); c.start_rev(); print('after stop REV=',c.rev)
s=StarDelta()
for t in [0,1,2.9,3.05,3.2,5]: print(t,s.state(t))