#!/bin/bash

set -e

for i in {1..100}
do
  /usr/bin/uuidgen
done > guids.list
