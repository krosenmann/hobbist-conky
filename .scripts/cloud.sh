#!/bin/bash

used=`megadf | grep Used | grep -oE "[0-9]{1,}"`
total=`megadf | grep Total | grep -oE "[0-9]{1,}"`
let "cloudStat = used * 100 / total"
echo $cloudStat

