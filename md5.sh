#!/bin/env bash
find ./tests -type f -name "test_*.py" -exec md5sum {} + | tee checksum.md5
