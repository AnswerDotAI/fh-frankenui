#!/usr/bin/env bash
llms_txt2ctx nbs/llms.txt --optional true >nbs/llms-ctx-full.txt
llms_txt2ctx nbs/llms.txt >nbs/llms-ctx.txt

# Need to remove Pico CSS stuff from context files
pysym2md --output_file nbs/apilist.txt fh_frankenui
