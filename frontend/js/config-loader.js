async function loadConfig() {
  const response = await fetch("/config/tools.config.json");
  return await response.json();
}

// Example usage
loadConfig().then((config) => {
  console.log("Loaded config:", config);
});
