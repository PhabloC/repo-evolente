const path = require("node:path");

const quote = (value) => `'${value.replace(/'/g, "'\\''")}'`;
const toRepoRelative = (file) =>
  path.relative(process.cwd(), file).split(path.sep).join("/");

const toStackFiles = (files, stackDir) =>
  files
    .map(toRepoRelative)
    .filter((file) => file.startsWith(`${stackDir}/`))
    .map((file) => path.relative(stackDir, file))
    .filter(Boolean)
    .map(quote);

const stackCommand = (stackDir, command, files) => {
  const stackFiles = toStackFiles(files, stackDir);

  if (stackFiles.length === 0) {
    return [];
  }

  return `cd ${quote(stackDir)} && ${command} ${stackFiles.join(" ")}`;
};

module.exports = {
  "front-end/**/*.{js,jsx,ts,tsx}": (files) =>
    stackCommand("front-end", "npm exec eslint -- --fix", files),
  "backend/**/*.{js,ts}": (files) =>
    stackCommand("backend", "npm exec eslint -- --fix", files),
  "mobile/**/*.{js,jsx,ts,tsx}": (files) =>
    stackCommand("mobile", "npm exec eslint -- --fix", files),
  "next-js/**/*.{js,jsx,ts,tsx}": (files) =>
    stackCommand("next-js", "npm exec eslint -- --fix", files),
  "*.{js,json,md,yml,yaml}": "prettier --write",
  ".github/**/*.{yml,yaml,md}": "prettier --write",
  "docs/**/*.{md,json,yml,yaml}": "prettier --write",
  "tasks/**/*.{md,json,yml,yaml}": "prettier --write",
  "scripts/**/*.js": "prettier --write",
};
