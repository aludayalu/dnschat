from dnslib.server import DNSServer, BaseResolver
from dnslib import RR, QTYPE, TXT

class EchoResolver(BaseResolver):
    def resolve(self, request):
        qname = request.q.qname
        labels = str(qname).rstrip('.').split('.')
        msg = labels[0]
        reply_msg = f"Echoing {msg}"
        reply = request.reply()
        reply.add_answer(RR(qname, QTYPE.TXT, rdata=TXT(reply_msg), ttl=60))
        return reply

resolver = EchoResolver()
server = DNSServer(resolver, port=53, address="0.0.0.0")
server.start()