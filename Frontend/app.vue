<template>
  <UApp>
    <NuxtPage />
  </UApp>
</template>

<script setup>
useHead({
  title: "BrainPath - Alzheimer Tespit Sistemi",
  meta: [
    { charset: "utf-8" },
    { name: "viewport", content: "width=device-width, initial-scale=1" },
    {
      name: "description",
      content:
        "BrainPath, yapay zeka destekli Alzheimer hastalığı tespit sistemi. Erken teşhis için güvenilir ve hızlı çözüm.",
    },
    {
      name: "keywords",
      content: "alzheimer, yapay zeka, sağlık, teşhis, beyin, nöroloji",
    },
    { name: "author", content: "BrainPath Team" },
    { property: "og:title", content: "BrainPath - Alzheimer Tespit Sistemi" },
    {
      property: "og:description",
      content:
        "BrainPath, yapay zeka destekli Alzheimer hastalığı tespit sistemi. Erken teşhis için güvenilir ve hızlı çözüm.",
    },
    { property: "og:type", content: "website" },
    { name: "theme-color", content: "#ffffff" },
  ],
});
</script>
