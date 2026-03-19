A collection of tools helpful in the opensourcing process.

### contributors.py
List unique contributors for a git repository

locally:
```
> python .\contributors.py --dir ..\io\

Reading git repo ..\io\

----- CONTRIBUTERS (username email) -----
CCP Games' Robot Minion robot
teamcity teamcity
CCP ChargeBack 35330827+ccp-chargeback@users.noreply.github.com
CCP Aporia 28982391+CCP-Aporia@users.noreply.github.com
CCP Toebeans 105929497+ccptoebeans@users.noreply.github.com
Ccp Toebeans ccptoebeans
Hrafn 5185245+hrafn@users.noreply.github.com
ccptoebeans
ccp-serpent 162123512+ccp-serpent@users.noreply.github.com
```

remotely:
```
> python .\contributors.py --url git@github.com:carbonengine/io.git

cloning from git@github.com:carbonengine/io.git
Cloning into 'OSCHECKER_TMP_DIR'...
remote: Enumerating objects: 2262, done.
remote: Counting objects: 100% (2262/2262), done.
remote: Compressing objects: 100% (810/810), done.
remote: Total 2262 (delta 1422), reused 2228 (delta 1398), pack-reused 0 (from 0)
Receiving objects: 100% (2262/2262), 1.35 MiB | 2.52 MiB/s, done.
Resolving deltas: 100% (1422/1422), done.

----- CONTRIBUTERS (username email) -----
CCP Games' Robot Minion robot
Ccp Toebeans ccptoebeans
CCP Aporia 28982391+CCP-Aporia@users.noreply.github.com
CCP ChargeBack 35330827+ccp-chargeback@users.noreply.github.com
Hrafn 5185245+hrafn@users.noreply.github.com
ccp-serpent 162123512+ccp-serpent@users.noreply.github.com
ccptoebeans
CCP Toebeans 105929497+ccptoebeans@users.noreply.github.com
teamcity teamcity
```
