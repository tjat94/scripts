def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    with open('/usr/share/dict/words') as f1, open('/usr/share/dict/american-english') as f2:
        words1 = f1.readlines()
        words2 = f2.readlines()

    num_words = min(len(words1), len(words2))

    for i in range(num_words):
        firstWord = words1[i].strip()
        secondWord = words2[i].strip()
        engine.queue(target.req, [firstWord, secondWord])

def handleResponse(req, interesting):
    if req.status != 404:
        table.add(req)
