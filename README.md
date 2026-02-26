### Cloud-Based Bankruptcy Prediction System


## What is this?
I wrote a Python script using Boto3 to automatically set up my AWS storage. Instead of clicking many buttons in the AWS website, my code does everything in one second.

## What my code does:

Creates 3 Buckets: It makes three different storage areas called raw, proceed, and final.

Adds Security: It turns on KMS Encryption. This means my files are locked and safe.

Uploads a File: It takes a file from my computer and puts it safely into the raw bucket.

## Why I built this:
I am learning how to be a Cloud Engineer! I built this because:

It's faster than doing it by hand.

It's safer because the code doesn't make "human mistakes."

It helps me manage many buckets (like 30 or 50) at the same time.

## How to use it:

Install Python and Boto3.

Put your AWS keys in your computer.

Run the script: la12.py.
