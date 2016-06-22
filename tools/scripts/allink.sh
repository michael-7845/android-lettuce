#!/bin/sh
FACILITY=`cat /root/_myFacilityLocation`
BASE=`python $FACILITY/_myfacility.py -b`
CUR=`pwd`

#al_config -> /home/ckt/lettuce/tools/myconfig.sh
if [ ! -e /usr/bin/al_config ]; then
  ln -s $BASE/tools/myconfig.sh /usr/bin/al_config
fi
#al_image -> /home/ckt/lettuce/tools/myimages.py
if [ ! -e /usr/bin/al_image ]; then
  ln -s $BASE/tools/myimages.py /usr/bin/al_image
fi
#al_imgtool -> /home/ckt/lettuce/tools/imgtool/start_imgtool.sh
if [ ! -e /usr/bin/al_imgtool ]; then
  ln -s $BASE/tools/imgtool/start_imgtool.sh /usr/bin/al_imgtool
fi
#al_new -> /home/ckt/lettuce/tools/create_project.sh
if [ ! -e /usr/bin/al_new ]; then
  ln -s $BASE/tools/create_project.sh /usr/bin/al_new
fi
#al_recorder -> /home/ckt/lettuce/tools/rectool/start_rectool.sh
if [ ! -e /usr/bin/al_recorder ]; then
  ln -s $BASE/tools/rectool/start_rectool.sh /usr/bin/al_recorder 
fi
#al_steps -> /home/ckt/lettuce/tools/showsteps.py
if [ ! -e /usr/bin/al_steps ]; then
  ln -s $BASE/tools/showsteps.py /usr/bin/al_steps 
fi
#al_update -> /home/ckt/lettuce/tools/update_project.sh
if [ ! -e /usr/bin/al_update ]; then
  ln -s $BASE/tools/update_project.sh /usr/bin/al_update
fi

