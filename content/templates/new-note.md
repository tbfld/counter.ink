<%*
// Prompt for folder location with default
const folders = [
  "content/blg/new",
  "content/blg/old",
  "content/blg",
  "content",
  "content/micro",
  "content/txt",
  "content/lib",
  "content/obj",
  "content/stat"
];

const selectedFolder = await tp.system.suggester(folders, folders, false, "Choose folder location:");
const targetFolder = selectedFolder || "content/blg/new";

// Get current date in YYYY-MM-DD format
const datePrefix = tp.date.now("YYYY-MM-DD");

// Prompt for note name (without date prefix)
const noteName = await tp.system.prompt("Note name (date will be added automatically):");

if (!noteName) {
  throw new Error("Note name is required");
}

// Create the full filename
const fileName = `${datePrefix}-${noteName}`;

// Move file to target folder with new name
await tp.file.move(`${targetFolder}/${fileName}`);

// Now insert the YAML headers
-%>
---
yaml_begin: true
title: <% tp.file.title.replace(/-/g, ' ').replace(/^(\d{4}) (\d{2}) (\d{2}) /, '$1-$2-$3 ') %>
description: <% tp.system.prompt("Description") %>
extract: "<% tp.system.prompt("Extract (brief quote/summary)") %>"
created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
updated: <% tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>
author: tb
images: false
order:
enableToc: true
permalink:
aliases:
publish: true
date: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - <% tp.system.prompt("Primary tag") %>
  - <% tp.system.prompt("Secondary tag (optional)", "") %>
status:
RSS: "<% tp.system.prompt("Include in RSS?", "true") %>"
yaml_end: true
---

<% tp.file.cursor(1) %>
