import json
from collections import defaultdict as dd
from PyQt5 import QtWidgets, QtCore

posts = dd()
class Post(QtWidgets.QListWidgetItem):
    """docstring for Post."""
    def __init__(self, question, answer, votes):
        super(Post, self).__init__()
        self.question = question
        self.answer = answer
        self.subposts = dd()
        self.superposts=dd()

        #vote count
        self.vc=votes[0]
        self.vi=votes[1]
        self.vl=votes[2]

        self.reccomends=dd()

        s='\t'
        if len(self.answer)>20:
            s+= self.answer[:20] +'...'
        else:
            s+= self.answer
        self.setText(s)

    def __post__(self,subs,recs=[]):
        for i in range(0,len(subs)):
            p = list(posts.keys())[subs[i][0]]
            if p not in self.subposts:
                self.subposts[p]=[]
            for a in subs[i][1:]:
                self.subposts[p].append(posts[p][a])
        for i in range(0,len(recs)):
            p = list(posts.keys())[recs[i][0]]
            if p not in self.reccomends:
                self.reccomends[p]=[]
            for a in recs[i][1:]:
                self.reccomends[p].append(list(posts.values())[a])
        for key in self.subposts:
            for sub in self.subposts[key]:
                if self.question not in sub.superposts:
                    sub.superposts[self.question]=[]
                if self not in sub.superposts[self.question]:
                    sub.superposts[self.question].append(self)

mess=json.loads(open('posts.json').read())
for p in mess:
    for a in mess[p]:
        if p not in posts:
            posts[p]=[]
        if len(a)==3:
            posts[p].append(Post(p,a[0],a[2]))
        elif len(a)==2:
            posts[p].append(Post(p,a[0],a[1]))

for p in posts:
    for i in range(len(posts[p])):
        a=mess[p][i]
        if len(a)==3:
            posts[p][i].__post__(a[1])
        elif len(a)==4:
            posts[p][i].__post__(a[1],a[3])

def search(query):
    global posts
    results = []
    for p in posts:
        if query in p:
            results.append(p)
    return results
