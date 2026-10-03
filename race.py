def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
               engine=Engine.THREADED,
               concurrentConnections=30,
               requestsPerConnection=100,
               pipeline=False
                   )
    for i in range(30):
        engine.queue(target.req, target.baseInput, gate='race1')
        engine.openGate('race1')
        engine.complete(timeout=60)

def handleResponse(req, interesting):
    table.add(req)