---
layout: default
title: Table-generation scripts
description: Scripts for generating TRMG lookup tables from the BIP-39 English word list.
permalink: /scripts/
---

## Table-generation scripts

These scripts generate Markdown lookup tables from the BIP-39 English word list in `english.txt`. Run them from the repository root with Python 3. Redirect the output to a separate file when you want to inspect or update a table.

|Script|Method|Output|
|------|------|------|
|`create_table_bin.py`|Binary values|The 2,048 BIP-39 words indexed by 11 bits.|
|`create_table_8ff.py`|D8/D16/D16|The lookup table for one D8 and two D16 dice.|
|`create_table_888cc.py`|D8/D8/D8/coin/coin|The lookup table for three D8 dice and two coins.|

## Commands

```bash
python3 scripts/create_table_bin.py > /tmp/binary-table.md
python3 scripts/create_table_8ff.py > /tmp/d8ff-table.md
python3 scripts/create_table_888cc.py > /tmp/888cc-table.md
```

The binary table used by the guides is available at [tables/binary-table](../tables/binary-table/). When updating an embedded table, keep the page's YAML front matter and introductory text, and replace only the generated table rows.

## Word list

All scripts read `scripts/english.txt`, the 2,048-word English BIP-39 word list. Keep the word list next to the scripts so they can be run from any working directory.
