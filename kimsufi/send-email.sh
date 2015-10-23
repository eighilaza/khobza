#!/bin/bash

echo "A KS1 Server is available" | mail -s "KS1 Available" $EMAIL_TA3I
echo "sent email at `date`" >> $HOME/kimsufi/email.log
