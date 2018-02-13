import json
from collections import defaultdict as dd

posts = dd()
class Post(object):
    """docstring for Post."""
    def __init__(self, question, answer, subposts, votes, reccomends=[]):
        super(Post, self).__init__()
        self.question = question
        self.answer = answer
        self.subposts = subposts
        self.superposts=[]

        #vote count
        self.vc=votes[0]
        self.vi=votes[1]
        self.vl=votes[2]

        self.reccomends=reccomends

    def __post__(self):
        for i in range(0,len(self.subposts)):
            self.subposts[i]=list(posts.values())[self.subposts[i][0]][self.subposts[i][1]]
        for i in range(0,len(self.reccomends)):
            self.reccomends[i]=list(posts.values())[self.reccomends[i][0]][self.reccomends[i][1]]
        for sub in self.subposts:
            if self not in sub.superposts:
                sub.superposts.append(self)

mess=json.loads(open('posts.json').read())
for p in mess:
    for a in mess[p]:
        if p not in posts:
            posts[p]=[]
        if len(a)==4:
            posts[p].append(Post(p,a[0],a[1],a[2],a[3]))
        elif len(a)==3:
            posts[p].append(Post(p,a[0],a[1],a[2]))

for p in posts:
    for a in posts[p]:
        a.__post__()

def search(query):
    global posts
    results = []
    for p in posts:
        if query in p:
            results.append(p)
    return results
