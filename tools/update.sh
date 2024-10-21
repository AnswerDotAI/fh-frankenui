#!/usr/bin/env bash
llms_txt2ctx lib_nbs/llms.txt --optional true >lib_nbs/llms-ctx-full.txt
llms_txt2ctx lib_nbs/llms.txt >lib_nbs/llms-ctx.txt

# Need to remove Pico CSS stuff from context files
pysym2md --output_file lib_nbs/apilist.txt fh_frankenui
