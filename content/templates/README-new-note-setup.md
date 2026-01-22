# New Note Template Setup Instructions

(TB: This note created 2026-01-21 w/ Claude Code via VS Code with the Cline plugin)

This guide explains how to use the `new-note.md` template to quickly create dated notes in Obsidian with proper YAML headers.

## Prerequisites

You must have the **Templater** plugin installed in Obsidian.

1. Open Obsidian Settings
2. Go to Community Plugins
3. Search for "Templater"
4. Install and Enable it

## Templater Configuration

1. Open Obsidian Settings → Templater
2. Set the **Template folder location** to: `content/templates`
3. Enable **Trigger Templater on new file creation** (optional, but recommended)
4. Enable **Enable System Commands** (required for the template to work)

## How to Use

### Method 1: Command Palette (Recommended)

1. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows/Linux) to open the command palette
2. Type "Templater: Create new note from template"
3. Select the `new-note` template
4. Follow the prompts:
   - **Choose folder location**: Select where to save (default: `content/blg/new`)
   - **Note name**: Enter the note name (date will be added automatically)
   - **Description**: Enter a description
   - **Extract**: Enter a brief quote or summary
   - **Primary tag**: Enter the main tag
   - **Secondary tag**: Enter optional second tag (or leave empty)
   - **Include in RSS**: Enter "true" or "false"

### Method 2: Add a Hotkey

1. Open Obsidian Settings → Hotkeys
2. Search for "Templater: Create new note from template"
3. Set your preferred keyboard shortcut (e.g., `Cmd+Shift+N`)
4. Now you can press your hotkey to quickly create a new note

## What the Template Does

1. **Prompts for folder location** with these options:
   - content/blg/new (default)
   - content/blg/old
   - content/blg
   - content
   - content/micro
   - content/txt
   - content/lib
   - content/obj
   - content/stat

2. **Automatically adds date prefix** in YYYY-MM-DD format (e.g., `2026-01-21-my-note.md`)

3. **Inserts YAML headers** with:
   - Auto-formatted title (converts date and hyphens to proper format)
   - Dynamic created/updated timestamps
   - Date field matching the filename date
   - All standard fields from your template
   - Interactive prompts for description, extract, tags, etc.

4. **Places cursor** in the content area ready for you to start writing

## Example Workflow

1. Press `Cmd+P` (or your hotkey)
2. Select "Templater: Create new note from template" → `new-note`
3. Select `content/blg/new` (or press Enter for default)
4. Enter note name: `my-thoughts-on-obsidian`
5. Fill in the prompts for description, extract, tags, etc.
6. Result: File created at `content/blg/new/2026-01-21-my-thoughts-on-obsidian.md` with all YAML headers populated

## Troubleshooting

- **Template not showing up**: Check that Templater's template folder is set to `content/templates`
- **Prompts not working**: Ensure "Enable System Commands" is enabled in Templater settings
- **File not moving to correct folder**: Make sure the folder paths exist in your vault

## Customization

To modify the available folders, edit the `folders` array at the top of `content/templates/new-note.md`.
