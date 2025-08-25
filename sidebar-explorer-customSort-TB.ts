export const customSortFn = (a: any, b: any) => {
  console.log(`Sorting item: ${a.name} (${a.isFolder ? "Folder" : "File"}) vs ${b.name} (${b.isFolder ? "Folder" : "File"})`);

  // Top-level order
  const nameOrderMap = {
    "about": 1,
    "recent_notes": 2,
    "microblog": 3,
    "blg": 4,
    "txt": 5,
    "obj": 6,
  };

  // Recognize date-based names (YYYY or YYYY-MM-DD)
  const datePattern = /^(19|20)\d{2}(-\d{2})?(-\d{2})?/;

  if (!a?.name || !b?.name) return 0;

  const orderA = nameOrderMap[a.name as keyof typeof nameOrderMap] || 1000;
  const orderB = nameOrderMap[b.name as keyof typeof nameOrderMap] || 1000;

  // Sort top-level items first
  if (orderA !== 1000 && orderB !== 1000) {
    console.log(`Sorting top-level: ${a.name} (${orderA}) vs ${b.name} (${orderB})`);
    return orderA - orderB;
  }

  const isYearA = datePattern.test(a.name);
  const isYearB = datePattern.test(b.name);

  // Reverse-sort year folders/files (newest first)
  if (isYearA && isYearB) {
    console.log(`Sorting year folders: ${b.name} vs ${a.name}`);
    return b.name.localeCompare(a.name); 
  }

  // Ensure folders appear before files
  if (a.isFolder && !b.isFolder) return -1;
  if (!a.isFolder && b.isFolder) return 1;

  return a.name.localeCompare(b.name);
};
