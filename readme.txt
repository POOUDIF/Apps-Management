DB PORTS :
============
10000   -> bbi apps (old, will be deprecated)
10001   -> dwh, master
10002   -> default (core-apps / django), various apps (ppcm, plm, sfc, insp, etc)
20000   -> integration, etlprocess, services
20001   -> notifications

include bbicorelib to project by using command : 
git submodule add git@gitlab.com:bbi-development/bbicorelib.git ./library