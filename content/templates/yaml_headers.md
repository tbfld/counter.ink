---
yaml_begin: true
title: <% tp.file.title.replace(/-/g, ' ').replace(/^(\d{4}) (\d{2}) (\d{2}) /, '$1-$2-$3 ') %>
description: <% tp.system.prompt("Description") %>
extract: "<% tp.system.prompt("Extract (brief quote/summary)") %>"
created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
updated: <% tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>
author: "tb"
images: "false"
order:
enableToc: "true"
permalink:
aliases:
draft: "true"
publish: "false"
date: <%* 
const dateMatch = tp.file.title.match(/^(\d{4}-\d{2}-\d{2})/);
tR += dateMatch ? dateMatch[1] : tp.date.now("YYYY-MM-DD");
%>
tags:
  - <% tp.system.prompt("Primary tag") %>
  - <% tp.system.prompt("Secondary tag (optional)", "") %>
status:
RSS: "<% tp.system.prompt("Include in RSS?", "true") %>"
yaml_end: true
---