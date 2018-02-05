import random

from recruit.tools.agents import USER_AGENT_LIST


# Change randomly user-agent
class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            print 'useragent:'+ua
            request.headers.setdefault('User-Agent', ua)
