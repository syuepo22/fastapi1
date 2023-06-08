#!/bin/sh


cmd="$@"

echo "Waiting for syuepo22 Server..."
while ! nc -zv $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "Connected to syuepo22 Server"
exec $cmd
