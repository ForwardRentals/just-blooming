#!/usr/bin/env python3
"""Wrap just-blooming.html (the artifact source) into a standalone index.html for GitHub Pages."""
from pathlib import Path
here = Path(__file__).parent
body = (here / 'just-blooming.html').read_text()
favicon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 120'%3E"
           "%3Ccircle cx='60' cy='60' r='56' fill='%23F4F0E8'/%3E%3Ccircle cx='60' cy='60' r='44' fill='none' stroke='%232A2B26' stroke-width='5'/%3E"
           "%3Cpath d='M60 70C46 60 46 42 60 28C74 42 74 60 60 70ZM60 70C44 68 34 60 26 52C42 50 54 58 60 70ZM60 70C76 68 86 60 94 52C78 50 66 58 60 70Z' fill='%23D6C24A' stroke='%232A2B26' stroke-width='3'/%3E%3C/svg%3E")
head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="icon" href="{favicon}">
<meta property="og:title" content="Just Blooming · Analogue PEMF in Squamish">
<meta property="og:description" content="A quiet PEMF practice among the trees in Squamish, BC.">
<meta property="og:image" content="img/jb-moss-hero-sm.jpg">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}[hidden]{{display:none!important}}</style>
'''
# title/meta/fonts/style from the artifact source belong in <head>; everything from the first <svg> on is body
cut = body.index('<svg width="0"')
(here / 'index.html').write_text(head + body[:cut] + '</head>\n<body>\n' + body[cut:] + '\n</body>\n</html>\n')
print('wrote index.html')
