<%*
// Standalone Index Page Updater
// Adds current note to content/blg/new/new.md index page
// Assumes note already has complete YAML frontmatter

const INDEX_FILE_PATH = "content/blg/new/new.md";
const INSERTION_MARKER = "<!-- RECENT_POSTS_START -->";

// Get current note info
const currentFile = app.workspace.getActiveFile();
if (!currentFile) {
    new Notice("❌ No active file found");
    return;
}
const noteContent = await app.vault.read(currentFile);

// Extract title and description from YAML frontmatter
const yamlMatch = noteContent.match(/---\n([\s\S]*?)\n---/);
if (!yamlMatch) {
    new Notice("❌ No YAML frontmatter found in current note");
    return;
}

const yamlContent = yamlMatch[1];
const titleMatch = yamlContent.match(/^title:\s*(.+)$/m);
const descriptionMatch = yamlContent.match(/^description:\s*(.+)$/m);

if (!titleMatch) {
    new Notice("❌ No title found in YAML frontmatter");
    return;
}

if (!descriptionMatch) {
    new Notice("❌ No description found in YAML frontmatter");
    return;
}

const noteTitle = titleMatch[1];
const noteDescription = descriptionMatch[1];
const noteFilename = currentFile.basename;

// Create the index entry
const indexEntry = `

> [!note]+ [[${noteFilename}|${noteTitle}]]
> ${noteDescription}`;

// Read and update the index file
const indexFile = tp.file.find_tfile(INDEX_FILE_PATH);
if (!indexFile) {
    new Notice(`❌ Could not find index file: ${INDEX_FILE_PATH}`);
    return;
}

const indexContent = await app.vault.read(indexFile);

// Find insertion point
const insertionIndex = indexContent.indexOf(INSERTION_MARKER);
if (insertionIndex === -1) {
    new Notice(`❌ Could not find ${INSERTION_MARKER} in index file`);
    return;
}

// Insert new entry at the top of the list
const insertionPoint = insertionIndex + INSERTION_MARKER.length;
const updatedIndexContent = 
    indexContent.slice(0, insertionPoint) + 
    indexEntry + 
    indexContent.slice(insertionPoint);

// Save the updated index
await app.vault.modify(indexFile, updatedIndexContent);

console.log("✅ Successfully updated index file");
new Notice(`✅ Added "${noteTitle}" to index page`);

// Also update content/recent.md
console.log("🔍 Starting recent.md update...");
const RECENT_FILE_PATH = "content/recent.md";
const RECENT_INSERTION_MARKER = "<!-- RECENT_POSTS_START -->";

console.log("📁 Looking for file:", RECENT_FILE_PATH);

// Read the recent file
const recentFile = app.vault.getAbstractFileByPath(RECENT_FILE_PATH);
if (!recentFile) {
    console.log("❌ Recent file not found at:", RECENT_FILE_PATH);
    new Notice(`❌ Could not find recent file: ${RECENT_FILE_PATH}`);
    return;
}

console.log("✅ Recent file found, reading content...");
const recentContent = await app.vault.read(recentFile);

// Find insertion point in recent file
const recentInsertionIndex = recentContent.indexOf(RECENT_INSERTION_MARKER);
console.log("📍 Marker found at index:", recentInsertionIndex);

if (recentInsertionIndex === -1) {
    new Notice(`❌ Could not find <!-- RECENT_POSTS_START --> marker in recent file`);
    return;
}

console.log("✅ Marker found, creating entry...");

// Insert new entry after the marker
const recentInsertionPoint = recentInsertionIndex + RECENT_INSERTION_MARKER.length;
const recentEntry = `
> [!note]+ [[${noteFilename}|${noteTitle}]]
> ${noteDescription}`;

const updatedRecentContent = 
    recentContent.slice(0, recentInsertionPoint) + 
    recentEntry + 
    recentContent.slice(recentInsertionPoint);

console.log("💾 Saving updated recent file...");

// Save the updated recent file
await app.vault.modify(recentFile, updatedRecentContent);

console.log("✅ Recent file updated successfully!");
new Notice(`✅ Also added "${noteTitle}" to recent page`);
-%>