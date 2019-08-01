from mitmproxy import ctx

def request(flow):
    # print(flow.request.headers)
    ctx.log.info(str(flow.request.headers))
    ctx.log.warn(str(flow.request.headers))
    ctx.log.error(str(flow.request.url))
    ctx.log.error(str(flow.request.host))
    ctx.log.error(str(flow.request.method))
    ctx.log.error(str(flow.request.path))

def response(flow):
    ctx.log.error(str(flow.response.status_code))
    ctx.log.error(str(flow.response.text))