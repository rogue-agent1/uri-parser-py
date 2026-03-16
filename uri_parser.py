#!/usr/bin/env python3
"""URI parser — RFC 3986 compliant decomposition."""
import re
class URI:
    def __init__(self,scheme=None,userinfo=None,host=None,port=None,path="",query=None,fragment=None):
        self.scheme=scheme;self.userinfo=userinfo;self.host=host;self.port=port
        self.path=path;self.query=query;self.fragment=fragment
    @classmethod
    def parse(cls,uri):
        m=re.match(r'^(?:([a-zA-Z][a-zA-Z0-9+.-]*):)?(?://(?:([^@]*)@)?([^:/?#]*)(?::(\d+))?)?([^?#]*)(?:\?([^#]*))?(?:#(.*))?$',uri)
        if not m:raise ValueError(f"Invalid URI: {uri}")
        port=int(m[4]) if m[4] else None
        return cls(m[1],m[2],m[3],port,m[5],m[6],m[7])
    def __str__(self):
        s=""
        if self.scheme:s+=f"{self.scheme}:"
        if self.host is not None:
            s+="//"
            if self.userinfo:s+=f"{self.userinfo}@"
            s+=self.host
            if self.port:s+=f":{self.port}"
        s+=self.path
        if self.query:s+=f"?{self.query}"
        if self.fragment:s+=f"#{self.fragment}"
        return s
    def query_params(self):
        if not self.query:return{}
        params={}
        for pair in self.query.split("&"):
            if "=" in pair:k,v=pair.split("=",1);params[k]=v
            else:params[pair]=""
        return params
def main():
    u=URI.parse("https://user:pass@example.com:8080/path?q=1&r=2#frag")
    print(f"Host: {u.host}, Port: {u.port}, Params: {u.query_params()}")
if __name__=="__main__":main()
