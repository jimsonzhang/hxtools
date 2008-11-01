#!/bin/bash

. /etc/hxloginpref.conf >/dev/null 2>/dev/null || :;

if [ "$AAA_HXTOOLS" == "yes" ]; then

# --- main big block ---

isroot=0;
[ "$UID" -eq 0 ] && isroot=1;

export CVS_RSH="ssh";
[ -n "$EDITOR" ] && export EDITOR;

# The typical SUSE path is cluttered with too much crap

# /usr/local comes first, naturally because that's the overriding things
if [ "$isroot" -ne 0 ]; then
	PATH="/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin:/opt/hxtools/bin:/usr/X11R6/bin";
else
	PATH="/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/opt/hxtools/bin:/usr/X11R6/bin";
fi;
for i in gnome2 gnome kde3; do
	[ -d "/opt/$i/bin" ] && PATH="$PATH:/opt/$i/bin";
done;
export PATH;

if [ "$COLORS" == yes ]; then
	#
	# See if grep knows about --color, and set inverse-cyan
	#
	grep --color=auto x /dev/null &>/dev/null;
	[ "$?" -ne 2 ] && alias grep="`which grep` --color=auto";
	export GREP_COLOR="36;7";
fi;

# Paths. Honors local setup.
#
if [ -e /etc/sysconfig/suseconfig ]; then
	. /etc/sysconfig/suseconfig;
	[ "$CWD_IN_ROOT_PATH" == yes -a "$isroot" -ne 0 ] && \
		export PATH="$PATH:.";
	[ "$CWD_IN_USER_PATH" == yes -a "$isroot" -eq 0 ] && \
		export PATH="$PATH:.";
fi;

# --- end big main block ---

fi; # if [ "$AAA_HXTOOLS" == "yes" ];