# Open Source Tools

A collection of tools helpful in the opensourcing process.

## contributors.py
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

### Using contributors.py to generate a mailmap file for `git filter-repo --mailmap`

It is useful to be able to generate a mailmap file to be used with the [git-filter-repo tool](https://github.com/newren/git-filter-repo)

`> python .\contributors.py --url git@github.com:carbonengine/io.git --mailmap .mailmap`

Will generate a `.mailmap` file containing all of the contributors to the io repo, unmapped:

```
Ccp Toebeans <ccptoebeans>
CCP ChargeBack <35330827+ccp-chargeback@users.noreply.github.com>
CCP Aporia <28982391+CCP-Aporia@users.noreply.github.com>
CCP Games' Robot Minion <robot>
Hrafn <5185245+hrafn@users.noreply.github.com>
CCP Toebeans <105929497+ccptoebeans@users.noreply.github.com>
ccp-serpent <162123512+ccp-serpent@users.noreply.github.com>
teamcity <teamcity>
ccptoebeans <>
```

`> python .\contributors.py --url git@github.com:carbonengine/io.git --mailmap .mailmap --anonymize`

Will generate the same `.mailmap` file, but with all the contributor information mapped to an anonymous user:

```
Anonymous CCP Employee <anonymous.employee@ccpgames.com> Ccp Toebeans <ccptoebeans>
Anonymous CCP Employee <anonymous.employee@ccpgames.com> CCP ChargeBack <35330827+ccp-chargeback@users.noreply.github.com>
Anonymous CCP Employee <anonymous.employee@ccpgames.com> CCP Aporia <28982391+CCP-Aporia@users.noreply.github.com>
Anonymous CCP Employee <anonymous.employee@ccpgames.com> CCP Games' Robot Minion <robot>
Anonymous CCP Employee <anonymous.employee@ccpgames.com> Hrafn <5185245+hrafn@users.noreply.github.com>
Anonymous CCP Employee <anonymous.employee@ccpgames.com> CCP Toebeans <105929497+ccptoebeans@users.noreply.github.com>
Anonymous CCP Employee <anonymous.employee@ccpgames.com> ccp-serpent <162123512+ccp-serpent@users.noreply.github.com>
Anonymous CCP Employee <anonymous.employee@ccpgames.com> teamcity <teamcity>
Anonymous CCP Employee <anonymous.employee@ccpgames.com> ccptoebeans <>
```

You can change the default anonymous email and username with the options `--anonusername` and `--anonemail`.

### Using git filter-repo with a mailmap file:

You must first install the the [git-filter-repo tool](https://github.com/newren/git-filter-repo). For both windows & mac this can be done through pip:

`> pip install git-filter-repo` 

To use the mailmap file to change contributor information:

```
> cd path/to/repo
> git filter-repo --mailmap path/to/.mailmap
```
You can now run the `contributors.py` script again to check that the contributor information has been changed. 

<span style="color:tomato">Note that you now have a history divergent from the main repo. You **MUST NOT** push these changes back up to the remote. This should only be done in order to create a fresh repo under the carbonengine/ organization.</span>
